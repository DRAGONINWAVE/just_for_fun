use std::f64::consts::PI;

mod nation {
    pub mod government {
        pub fn govern() {}
    }
    pub fn govern() {}
}
use crate::nation::govern as nation_govern;
use crate::nation::government::govern;

fn main() {
    govern();
    nation_govern();
    println!("{}", (PI / 2.0))
}
