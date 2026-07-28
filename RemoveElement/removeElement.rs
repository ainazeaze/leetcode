impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let count : i32 = nums.retain(|&e| e == val).len()
        for (e, i) in nums.iter().enumerate() {
            if e != val {
                nums[i] = val
            }
        }
    }
}
