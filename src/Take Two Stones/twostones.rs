fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn main() {
    let n = get_input().trim().parse::<usize>().unwrap();
    if n % 2 == 0 {
        println!("Bob");
    } else {
        println!("Alice");
    }
}