impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x < 2 {
            return x;
        }
        let x = x as i64;
        let mut l = 1;
        let mut r = x / 2;
        while l <= r {
            let m = l + (r - l) / 2;
            let m2: i64 = (m * m) as i64;
            if m2 == x {
                return m as i32;
            } else if m2 < x {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        r as i32
    }
}
