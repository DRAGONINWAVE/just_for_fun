fn main() {
    let s1 = String::from("hello world");
    let s2 = &s1;
    println!("s1 is {},s2 is {}", s1, s2);
    let s3 = String::from("hello");
    let len = calculate_length(&s3);
    println!("The length of '{}' is {}.", s3, len);
    let mut l1 = String::from("run");
    let l2 = &mut l1;
    l2.push_str("oob");
    println!("{}", l2);
}
fn calculate_length(s: &String) -> usize {
    s.len()
}
