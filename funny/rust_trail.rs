struct Person {
    name: String,
    age: u32,
}
trait Descriptive {
    fn describe(&self) -> String {
        String::from("[Object]")
    }
}
impl Descriptive for Person {
    fn describe(&self) -> String {
        format!("{} {}", self.name, self.age)
    }
}
fn main() {
    let cali = Person {
        name: String::from("Cali"),
        age: 24,
    };
    println!("{}", cali.describe());
}
