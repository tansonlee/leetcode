impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        let mut total_chairs = 0;
        for c in corridor.chars() {
            if c == 'S' {
                total_chairs += 1;
            }
        }

        if (total_chairs < 2) || (total_chairs % 2 != 0) {
            return 0;
        }

        let mut it = corridor.chars().peekable();
        let mut result: i64 = 1;

        while it.peek().is_some() {
            // Find 2 seats.
            while it.peek().is_some() && *it.peek().unwrap() != 'S' {
                it.next();
            }
            it.next();
            while it.peek().is_some() && *it.peek().unwrap() != 'S' {
                it.next();
            }
            it.next();

            // Count plants until the next chair.
            let mut num_plants = 0;
            while it.peek().is_some() && *it.peek().unwrap() == 'P' {
                it.next();
                num_plants += 1;
            }
            if it.peek().is_some() {
                println!("{}", num_plants);
                result *= (num_plants + 1);
                result %= (i64::pow(10, 9) + 7);
            }
        }

        result as i32
    }
}
