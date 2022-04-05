use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    for line in stdin.lock().lines().map(|l| l.unwrap()) {
        let nums: Vec<i64> = line.split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();
        let w = nums[0];
        let s = nums[1];
        let c = nums[2];
        let k = nums[3];
        if s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k) {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}