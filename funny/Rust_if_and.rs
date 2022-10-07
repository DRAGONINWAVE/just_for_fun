fn main() {
    let number = 3;
    if number < 5 {
        println!("条件为true");
    } else {
        println!("条件为False");
    }
    let a = 3;
    let number = if a > 0 { 1 } else { -1 };
    println!("number为{}", number);
}
