impl Solution {
    pub fn max_coins(piles: Vec<i32>) -> i32 {
        let mut piles_m = piles.clone();
        piles_m.sort();
        piles_m.reverse();

        let mut i = 1;
        let mut cnt = 0;
        let n = piles_m.len() / 3;
        let mut res = 0;

        while cnt < n {
            res += piles_m[i];
            i += 2;
            cnt += 1;
        }

        res
    }
}
