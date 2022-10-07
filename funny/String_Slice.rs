fn main() {
    let s = String::from("broadcast");
    let part1 = &s[0..5];
    let part2 = &s[5..];
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    let part = &arr[0..];
    for i in part.iter() {
        println!("{}", i);
    }
    println!("{}={}+{}", s, part1, part2);
}
