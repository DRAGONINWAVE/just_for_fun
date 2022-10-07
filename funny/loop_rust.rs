fn main() {
    let mut number = 1;
    while number != 4 {
        println!("{}", number);
        number = number + 1;
    }
    println!("EXIT");
    let mut i = 0;
    while i != 10 {
        i = i + 1;
        println!("i : {}", i)
    }
    let a = [10, 20, 30, 40, 50, 60];
    for x in a.iter() {
        println!("a 的 iter 值为{}", x);
    }
    let s = ['R', 'U', 'N', 'O', 'O', 'B'];
    let mut i = 0;
    loop {
        let ch = s[i];
        if ch == 'O' {
            break;
        }
        println!("\'{}\'", ch);
        i = i + 1;
    }
    let location = loop {
        let ch = s[i];
        if ch == 'O' {
            break i;
        }
        i = i + 1;
    };
    println!("\'O'\'的索引为{}", location);
}
