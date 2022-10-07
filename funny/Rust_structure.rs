#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 32,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 40,
        height: 50,
    };
    println!("rect1: {:?}", rect1);
    println!("rect1's area is {}", rect1.area());
    println!("rect1 is wider rect2 is {}", rect1.wider(&rect2));
    let rect = Rectangle::create(30, 50);
    println!("rect {:?}", rect);
}
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn wider(&self, rect: &Rectangle) -> bool {
        self.width > rect.width
    }
    fn create(width: u32, height: u32) -> Rectangle {
        Rectangle { width, height }
    }
}
