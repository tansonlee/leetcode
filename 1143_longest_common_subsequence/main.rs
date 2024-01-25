use std::collections::HashMap;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let mut memo = HashMap::new();
        
        fn helper(text1: &String, text2: &String, i: usize, j: usize, memo: &mut HashMap<(usize, usize), i32>) -> i32 {
            if memo.contains_key(&(i, j)) {
                return *memo.get(&(i, j)).unwrap();
            }
            if i >= text1.len() || j >= text2.len() {
                memo.insert((i, j), 0);
                return 0;
            }
            if text1.as_bytes()[i] == text2.as_bytes()[j] {
                let val = 1 + helper(text1, text2, i + 1, j + 1, memo);
                memo.insert((i, j), val);
                return val;
            }

            let val = std::cmp::max(helper(text1, text2, i + 1, j, memo), helper(text1, text2, i, j + 1, memo));
            memo.insert((i, j), val);
            val
        }

        helper(&text1, &text2, 0, 0, &mut memo)
    }
}
