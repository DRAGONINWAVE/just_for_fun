fn longer<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}
fn main() {
    let r;
    {
        let s1 = "qqqq";
        let s2 = "vvvvvvvv";
        r = longer(s1, s2);
    }
    println!("{} is longer", r);
}
