use core::num::NonZeroUsize;
use std::{convert::TryFrom, str::FromStr};

#[macro_use]
pub mod error;
use error::*;

// Taken from https://github.com/Follpvosten/mudders

/// The functionality of the crate lives here.
///
/// A symbol table is, internally, a vector of valid ASCII bytes that are used
/// to generate lexicographically evenly-spaced strings.
#[derive(Clone, Debug)]
pub struct SymbolTable(Vec<u8>);

impl SymbolTable {
    /// Creates a new symbol table from the given byte slice.
    /// The slice is internally sorted using `.sort()`.
    ///
    /// An error is returned if one of the given bytes is out of ASCII range.
    pub fn new(source: &[u8]) -> Result<Self, CreationError> {
        ensure! { !source.is_empty(), CreationError::EmptySlice }
        ensure! { all_chars_ascii(&source), NonAsciiError::NonAsciiU8 }
        // Copy the values, we need to own them anyways...
        let mut vec: Vec<_> = source.iter().copied().collect();
        // Sort them so they're actually in order.
        // (You can pass in ['b', 'a'], but that's not usable internally I think.)
        vec.sort();
        vec.dedup();
        Ok(Self(vec))
    }

    /// Creates a new symbol table from the given characters.
    /// The slice is internally sorted using `.sort()`.
    ///
    /// An error is returned if one of the given characters is not ASCII.
    pub fn from_chars(source: &[char]) -> Result<Self, CreationError> {
        let inner: Box<[u8]> = source
            .iter()
            .map(|c| try_ascii_u8_from_char(*c))
            .collect::<Result<_, _>>()?;
        Ok(Self::new(&inner)?)
    }

    /// Returns a SymbolTable which contains the lowercase latin alphabet (`[a-z]`).
    #[allow(clippy::char_lit_as_u8)]
    pub fn alphabet() -> Self {
        Self::new(&('a' as u8..='z' as u8).collect::<Box<[_]>>()).unwrap()
    }

    /// Returns a SymbolTable which contains the digits (`[0-9]`) and lowercase letters (`[a-z]`).
    #[allow(clippy::char_lit_as_u8)]
    pub fn base36() -> Self {
        Self::new(
            &('0' as u8..='9' as u8)
                .chain('a' as u8..='z' as u8)
                .collect::<Box<[_]>>(),
        )
        .unwrap()
    }

    /// Returns a SymbolTable which contains the digits, lowercase, and uppercase letters (`[0-9a-zA-Z]`).
    #[allow(clippy::char_lit_as_u8)]
    pub fn base62() -> Self {
        Self::new(
            &('0' as u8..='9' as u8)
                .chain('A' as u8..='Z' as u8)
                .chain('a' as u8..='z' as u8)
                .collect::<Box<[_]>>(),
        )
        .unwrap()
    }

    /// Generate `amount` strings that lexicographically sort between `start` and `end`.
    /// The algorithm will try to make them as evenly-spaced as possible.
    ///
    /// When both parameters are empty strings, `amount` new strings that are
    /// in lexicographical order are returned.
    ///
    /// If parameter `b` is lexicographically before `a`, they are swapped internally.
    ///
    /// ```
    /// # use mudder::SymbolTable;
    /// # use std::num::NonZeroUsize;
    /// // Using the included alphabet table
    /// let table = SymbolTable::alphabet();
    /// // Generate 10 strings from scratch
    /// let results = table.mudder("", "", NonZeroUsize::new(10).unwrap()).unwrap();
    /// assert!(results.len() == 10);
    /// // results should look something like ["b", "d", "f", ..., "r", "t"]
    /// ```
    pub fn mudder(
        &self,
        a: &str,
        b: &str,
        amount: NonZeroUsize,
    ) -> Result<Vec<String>, GenerationError> {
        use error::InternalError::*;
        use GenerationError::*;
        ensure! { all_chars_ascii(a), NonAsciiError::NonAsciiU8 }
        ensure! { all_chars_ascii(b), NonAsciiError::NonAsciiU8 }
        ensure! { self.contains_all_chars(a), UnknownCharacters(a.to_string()) }
        ensure! { self.contains_all_chars(b), UnknownCharacters(b.to_string()) }
        let (a, b) = if a.is_empty() || b.is_empty() {
            // If an argument is empty, keep the order
            (a, b)
        } else if b < a {
            // If they're not empty and b is lexicographically prior to a, swap them
            (b, a)
        } else {
            // You can't generate values between two matching strings.
            ensure! { a != b, MatchingStrings(a.to_string()) }
            // In any other case, keep the order
            (a, b)
        };

        // TODO: Check for lexicographical adjacency!
        //ensure! { !lex_adjacent(a, b), LexAdjacentStrings(a.to_string(), b.to_string()) }

        // Count the characters start and end have in common.
        let matching_count: usize = {
            // Iterate through the chars of both given inputs...
            let (mut start_chars, mut end_chars) = (a.chars(), b.chars());
            // We need to keep track of this, because:
            // In the case of `a` == `"a"` and `b` == `"aab"`,
            // we actually need to compare `""` to `"b"` later on, not `""` to `"a"`.
            let mut last_start_char = '\0';
            // Counting to get the index.
            let mut i: usize = 0;
            loop {
                // Advance the iterators...
                match (start_chars.next(), end_chars.next()) {
                    // As long as there's two characters that match, increment i.
                    (Some(sc), Some(ec)) if sc == ec => {
                        last_start_char = sc;
                        i += 1;
                        continue;
                    }
                    // If start_chars have run out, but end_chars haven't, check
                    // if the current end char matches the last start char.
                    // If it does, we still need to increment our counter.
                    (None, Some(ec)) if ec == last_start_char => {
                        i += 1;
                        continue;
                    }
                    // break with i as soon as any mismatch happens or both iterators run out.
                    // matching_count will either be 0, indicating that there's
                    // no leading common pattern, or something other than 0, in
                    // that case it's the count of common characters.
                    (None, None) | (Some(_), None) | (None, Some(_)) | (Some(_), Some(_)) => {
                        break i
                    }
                }
            }
        };

        // Count the number to add to the total requests amount.
        // If a or b is empty, we need one item less in the pool;
        // two items less if both are empty.
        let non_empty_input_count = [a, b].iter().filter(|s| !s.is_empty()).count();
        // For convenience
        let computed_amount = || amount.get() + non_empty_input_count;

        // Calculate the distance between the first non-matching characters.
        // If matching_count is greater than 0, we have leading common chars,
        // so we skip those, but add the amount to the depth base.
        let branching_factor = self.distance_between_first_chars(
            //            v--- matching_count might be higher than a.len()
            //           vvv   because we might count past a's end
            &a[std::cmp::min(matching_count, a.len())..],
            &b[matching_count..],
        )?;
        // We also add matching_count to the depth because if we're starting
        // with a common prefix, we have at least x leading characters that
        // will be the same for all substrings.
        let mut depth =
            depth_for(dbg!(branching_factor), dbg!(computed_amount())) + dbg!(matching_count);

        // if branching_factor == 1 {
        //     // This should only be the case when we have an input like `"z", ""`.
        //     // In this case, we can generate strings after the z, but we need
        //     // to go one level deeper in any case.
        //     depth += 1;
        // }

        // TODO: Maybe keeping this as an iterator would be more efficient,
        // but it would have to be cloned at least once to get the pool length.
        let pool: Vec<String> = self.traverse("".into(), a, b, dbg!(depth)).collect();
        let pool = if (pool.len() as isize).saturating_sub(non_empty_input_count as isize)
            < amount.get() as isize
        {
            depth += depth_for(branching_factor, computed_amount() + pool.len());
            dbg!(self.traverse("".into(), a, b, dbg!(depth)).collect())
        } else {
            pool
        };
        if (pool.len() as isize).saturating_sub(non_empty_input_count as isize)
            < amount.get() as isize
        {
            // We still don't have enough items, so bail
            panic!(
                "Internal error: Failed to calculate the correct tree depth!
This is a bug. Please report it at: https://github.com/Follpvosten/mudders/issues
and make sure to include the following information:

Symbols in table: {symbols:?}
Given inputs: {a:?}, {b:?}, amount: {amount}
matching_count: {m_count}
non_empty_input_count: {ne_input_count}
required pool length (computed amount): {comp_amount}
branching_factor: {b_factor}
final depth: {depth}
pool: {pool:?} (length: {pool_len})",
                symbols = self.0.iter().map(|i| *i as char).collect::<Box<[_]>>(),
                a = a,
                b = b,
                amount = amount,
                m_count = matching_count,
                ne_input_count = non_empty_input_count,
                comp_amount = computed_amount(),
                b_factor = branching_factor,
                depth = depth,
                pool = pool,
                pool_len = pool.len(),
            )
        }
        Ok(if amount.get() == 1 {
            pool.get(pool.len() / 2)
                .map(|item| vec![item.clone()])
                .ok_or_else(|| FailedToGetMiddle)?
        } else {
            let step = computed_amount() as f64 / pool.len() as f64;
            let mut counter = 0f64;
            let mut last_value = 0;
            let result: Vec<_> = pool
                .into_iter()
                .filter(|_| {
                    counter += step;
                    let new_value = counter.floor() as usize;
                    if new_value > last_value {
                        last_value = new_value;
                        true
                    } else {
                        false
                    }
                })
                .take(amount.into())
                .collect();
            ensure! { result.len() == amount.get(), NotEnoughItemsInPool };
            result
        })
    }

    /// Convenience wrapper around `mudder` to generate exactly one string.
    ///
    /// # Safety
    /// This function calls `NonZeroUsize::new_unchecked(1)`.
    pub fn mudder_one(&self, a: &str, b: &str) -> Result<String, GenerationError> {
        self.mudder(a, b, unsafe { NonZeroUsize::new_unchecked(1) })
            .map(|mut vec| vec.remove(0))
    }

    /// Convenience wrapper around `mudder` to generate an amount of fresh strings.
    ///
    /// `SymbolTable.generate(amount)` is equivalent to `SymbolTable.mudder("", "", amount)`.
    pub fn generate(&self, amount: NonZeroUsize) -> Result<Vec<String>, GenerationError> {
        self.mudder("", "", amount)
    }

    /// Traverses a virtual tree of strings to the given depth.
    fn traverse<'a>(
        &'a self,
        curr_key: String,
        start: &'a str,
        end: &'a str,
        depth: usize,
    ) -> Box<dyn Iterator<Item = String> + 'a> {
        if depth == 0 {
            // If we've reached depth 0, we don't go futher.
            Box::new(std::iter::empty())
        } else {
            // Generate all possible mutations on the current depth
            Box::new(
                self.0
                    .iter()
                    .filter_map(move |c| -> Option<Box<dyn Iterator<Item = String>>> {
                        // TODO: Performance - this probably still isn't the best option.
                        let key = {
                            let the_char = *c as char;
                            let mut string =
                                String::with_capacity(curr_key.len() + the_char.len_utf8());
                            string.push_str(&curr_key);
                            string.push(the_char);
                            string
                        };

                        // After the end key, we definitely do not continue.
                        if key.as_str() > end && !end.is_empty() {
                            None
                        } else if key.as_str() < start {
                            // If we're prior to the start key...
                            // ...and the start key is a subkey of the current key...
                            if start.starts_with(&key) {
                                // ...only traverse the subtree, ignoring the key itself.
                                Some(Box::new(self.traverse(key, start, end, depth - 1)))
                            } else {
                                None
                            }
                        } else {
                            // Traverse normally, returning both the parent and sub key,
                            // in all other cases.
                            if key.len() < 2 {
                                let iter = std::iter::once(key.clone());
                                Some(if key == end {
                                    Box::new(iter)
                                } else {
                                    Box::new(iter.chain(self.traverse(key, start, end, depth - 1)))
                                })
                            } else {
                                let first = key.chars().next().unwrap();
                                Some(if key.chars().all(|c| c == first) {
                                    // If our characters are all the same,
                                    // don't add key to the list, only the subtree.
                                    Box::new(self.traverse(key, start, end, depth - 1))
                                } else {
                                    Box::new(std::iter::once(key.clone()).chain(self.traverse(
                                        key,
                                        start,
                                        end,
                                        depth - 1,
                                    )))
                                })
                            }
                        }
                    })
                    .flatten(),
            )
        }
    }

    fn distance_between_first_chars(
        &self,
        start: &str,
        end: &str,
    ) -> Result<usize, GenerationError> {
        use InternalError::WrongCharOrder;
        // check the first character of both strings...
        Ok(match (start.chars().next(), end.chars().next()) {
            // if both have a first char, compare them.
            (Some(start_char), Some(end_char)) => {
                ensure! { start_char < end_char, WrongCharOrder(start_char, end_char) }
                let distance =
                    try_ascii_u8_from_char(end_char)? - try_ascii_u8_from_char(start_char)?;
                distance as usize + 1
            }
            // if only the start has a first char, compare it to our last possible symbol.
            (Some(start_char), None) => {
                let end_u8 = self.0.last().unwrap();
                // In this case, we allow the start and end char to be equal.
                // This is because you can generate something after the last char,
                // but not before the first char.
                //                   vv
                ensure! { start_char <= *end_u8 as char, WrongCharOrder(start_char, *end_u8 as char) }
                let distance = end_u8 - try_ascii_u8_from_char(start_char)?;
                if distance == 0 {
                    2
                } else {
                    distance as usize + 1
                }
            }
            // if only the end has a first char, compare it to our first possible symbol.
            (None, Some(end_char)) => {
                let start_u8 = self.0.first().unwrap();
                ensure! { *start_u8 <= end_char as u8, WrongCharOrder(*start_u8 as char, end_char) }
                let distance = try_ascii_u8_from_char(end_char)? - start_u8;
                if distance == 0 {
                    2
                } else {
                    distance as usize + 1
                }
            }
            // if there's no characters given, the whole symboltable is our range.
            _ => self.0.len(),
        })
    }

    fn contains_all_chars(&self, chars: impl AsRef<[u8]>) -> bool {
        chars.as_ref().iter().all(|c| self.0.contains(c))
    }
}

/// Calculate the required depth for the given values.
///
/// `branching_factor` is used as the logarithm base, `n_elements` as the
/// value, and the result is rounded up and cast to usize.
fn depth_for(branching_factor: usize, n_elements: usize) -> usize {
    f64::log(n_elements as f64, branching_factor as f64).ceil() as usize
}

fn try_ascii_u8_from_char(c: char) -> Result<u8, NonAsciiError> {
    u8::try_from(c as u32).map_err(NonAsciiError::from)
}
fn all_chars_ascii(chars: impl AsRef<[u8]>) -> bool {
    chars.as_ref().iter().all(|i| i.is_ascii())
}

impl FromStr for SymbolTable {
    type Err = CreationError;
    fn from_str(s: &str) -> Result<Self, CreationError> {
        Self::from_chars(&s.chars().collect::<Box<[_]>>())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::num::NonZeroUsize;

    /// Create and unwrap a NonZeroUsize from the given usize.
    fn n(n: usize) -> NonZeroUsize {
        NonZeroUsize::new(n).unwrap()
    }

    // Public API tests:

    #[test]
    #[allow(clippy::char_lit_as_u8)]
    fn valid_tables_work() {
        assert!(SymbolTable::new(&[1, 2, 3, 4, 5]).is_ok());
        assert!(SymbolTable::new(&[125, 126, 127]).is_ok());
        // Possible, but to be discouraged
        assert!(SymbolTable::new(&['a' as u8, 'f' as u8]).is_ok());
        assert!(SymbolTable::from_chars(&['a', 'b', 'c']).is_ok());
        assert!(SymbolTable::from_str("0123").is_ok());
    }

    #[test]
    fn invalid_tables_error() {
        assert!(SymbolTable::from_str("🍅😂👶🏻").is_err());
        assert!(SymbolTable::from_chars(&['🍌', '🍣', '⛈']).is_err());
        assert!(SymbolTable::new(&[128, 129, 130]).is_err());
        assert!(SymbolTable::new(&[]).is_err());
        assert!(SymbolTable::from_chars(&[]).is_err());
        assert!(SymbolTable::from_str("").is_err());
    }

    #[test]
    fn unknown_chars_error() {
        use error::GenerationError::UnknownCharacters;
        // You cannot pass in strings with characters not in the SymbolTable:
        let table = SymbolTable::alphabet();
        assert_eq!(
            table.mudder_one("123", "()/"),
            Err(UnknownCharacters("123".into()))
        );
        assert_eq!(
            table.mudder_one("a", "123"),
            Err(UnknownCharacters("123".into()))
        );
        assert_eq!(
            table.mudder_one("0)(", "b"),
            Err(UnknownCharacters("0)(".into()))
        );
        let table = SymbolTable::from_str("123").unwrap();
        assert_eq!(
            table.mudder_one("a", "b"),
            Err(UnknownCharacters("a".into()))
        );
        assert_eq!(
            table.mudder_one("456", "1"),
            Err(UnknownCharacters("456".into()))
        );
        assert_eq!(
            table.mudder_one("2", "abc"),
            Err(UnknownCharacters("abc".into()))
        );
    }

    #[test]
    fn equal_strings_error() {
        use error::GenerationError::MatchingStrings;
        let table = SymbolTable::alphabet();
        assert_eq!(
            table.mudder_one("abc", "abc"),
            Err(MatchingStrings("abc".into()))
        );
        assert_eq!(
            table.mudder_one("xyz", "xyz"),
            Err(MatchingStrings("xyz".into()))
        );
    }

    // TODO: Make this test work.
    // I need to find out how to tell if two strings are lexicographically inseparable.
    // #[test]
    // fn lexicographically_adjacent_strings_error() {
    //     assert!(SymbolTable::alphabet().mudder("ba", "baa", n(1)).is_err());
    // }

    #[test]
    fn reasonable_values() {
        let table = SymbolTable::from_str("ab").unwrap();
        let result = table.mudder_one("a", "b").unwrap();
        assert_eq!(result, "ab");
        let table = SymbolTable::from_str("0123456789").unwrap();
        let result = table.mudder_one("1", "2").unwrap();
        assert_eq!(result, "15");
    }

    #[test]
    fn outputs_more_or_less_match_mudderjs() {
        let table = SymbolTable::from_str("abc").unwrap();
        let result = table.mudder_one("a", "b").unwrap();
        assert_eq!(result, "ac");
        let table = SymbolTable::alphabet();
        let result = table.mudder("anhui", "azazel", n(3)).unwrap();
        assert_eq!(result.len(), 3);
        assert_eq!(vec!["aq", "as", "av"], result);
    }

    #[test]
    fn empty_start() {
        let table = SymbolTable::from_str("abc").unwrap();
        let result = table.mudder("", "c", n(2)).unwrap();
        assert_eq!(result.len(), 2);
    }

    #[test]
    fn empty_end() {
        let table = SymbolTable::from_str("abc").unwrap();
        let result = table.mudder("b", "", n(2)).unwrap();
        assert_eq!(result.len(), 2);
    }

    #[test]
    fn generate_before_ax() {
        // While you can't generate anything before 'a' with alphabet(), you
        // should be able to generate something before "a" + something else.
        let table = SymbolTable::alphabet();
        let result = table.mudder("", "axxx", n(10)).unwrap();
        assert_eq!(result.len(), 10);
        assert!(result.iter().all(|k| k.as_str() > "a"));
        // Some more to be sure
        assert!(table.mudder_one("", "ab").is_ok());
        assert!(table.mudder_one("", "abc").is_ok());
    }

    #[test]
    fn generate_after_z() {
        let table = SymbolTable::alphabet();
        let result = table.mudder("z", "", n(10)).unwrap();
        assert_eq!(result.len(), 10);
        assert!(result.iter().all(|k| k.as_str() > "z"));
    }

    #[test]
    fn only_amount() {
        let table = SymbolTable::alphabet();
        let result = table.generate(n(10)).unwrap();
        assert_eq!(result.len(), 10);
    }

    #[test]
    fn values_sorting_correct() {
        let mut iter = SymbolTable::alphabet().generate(n(12)).into_iter();
        while let (Some(one), Some(two)) = (iter.next(), iter.next()) {
            assert!(one < two);
        }
    }

    #[test]
    fn differing_input_lengths() {
        let table = SymbolTable::alphabet();
        let result = table.mudder_one("a", "ab").unwrap();
        assert!(result.starts_with('a'));
    }

    #[test]
    fn values_consistently_between_start_and_end() {
        let table = SymbolTable::alphabet();
        {
            // From z to a
            let mut right = String::from("z");
            for _ in 0..500 {
                let new_val = dbg!(table.mudder_one("a", &right).unwrap());
                assert!(new_val < right);
                assert!(new_val.as_str() > "a");
                right = new_val;
            }
        }
        {
            // And from a to z
            let mut left = String::from("a");
            // TODO:    vv this test fails for higher numbers. FIXME!
            for _ in 0..17 {
                let new_val = dbg!(table.mudder_one(&left, "z").unwrap());
                assert!(new_val > left);
                assert!(new_val.as_str() < "z");
                left = new_val;
            }
        }
    }

    // Internal/private method tests:
    #[test]
    fn traverse_alphabet() {
        fn traverse_alphabet(a: &str, b: &str, depth: usize) -> Vec<String> {
            SymbolTable::alphabet()
                .traverse("".into(), a, b, depth)
                .collect()
        }
        assert_eq!(traverse_alphabet("a", "d", 1), vec!["a", "b", "c", "d"]);
        assert_eq!(
            traverse_alphabet("a", "z", 1),
            ('a' as u32 as u8..='z' as u32 as u8)
                .map(|c| (c as char).to_string())
                .collect::<Vec<_>>()
        );
        assert_eq!(
            traverse_alphabet("a", "b", 2),
            vec![
                "a", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an",
                "ao", "ap", "aq", "ar", "as", "at", "au", "av", "aw", "ax", "ay", "az", "b"
            ]
        )
    }

    #[test]
    fn traverse_custom() {
        fn traverse(table: &str, a: &str, b: &str, depth: usize) -> Vec<String> {
            let table = SymbolTable::from_str(table).unwrap();
            table.traverse("".into(), a, b, depth).collect()
        }
        assert_eq!(traverse("abc", "a", "c", 1), vec!["a", "b", "c"]);
        assert_eq!(
            traverse("abc", "a", "c", 2),
            vec!["a", "ab", "ac", "b", "ba", "bc", "c"]
        );
        assert_eq!(
            traverse("0123456789", "1", "2", 2),
            vec!["1", "10", "12", "13", "14", "15", "16", "17", "18", "19", "2"]
        );
    }

    #[test]
    fn distance_between_first_chars_correct() {
        let table = SymbolTable::alphabet();
        assert_eq!(table.distance_between_first_chars("a", "b").unwrap(), 2);
        assert_eq!(table.distance_between_first_chars("a", "z").unwrap(), 26);
        assert_eq!(table.distance_between_first_chars("", "").unwrap(), 26);
        assert_eq!(table.distance_between_first_chars("n", "").unwrap(), 13);
        assert_eq!(table.distance_between_first_chars("", "n").unwrap(), 14);
        assert_eq!(table.distance_between_first_chars("y", "z").unwrap(), 2);
        assert_eq!(table.distance_between_first_chars("a", "y").unwrap(), 25);
        assert_eq!(
            table.distance_between_first_chars("aaaa", "zzzz").unwrap(),
            table.distance_between_first_chars("aa", "zz").unwrap()
        );

        let table = SymbolTable::from_str("12345").unwrap();
        assert_eq!(table.distance_between_first_chars("1", "2").unwrap(), 2);
        assert_eq!(table.distance_between_first_chars("1", "3").unwrap(), 3);
        assert_eq!(table.distance_between_first_chars("2", "3").unwrap(), 2);
    }
}
