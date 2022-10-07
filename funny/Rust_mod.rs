mod nation {
    pub mod government {
        pub fn govern() {}
    }
    mod congress {
        pub fn legislate() {}
    }
    mod court {
        fn judicial() {
            super::congress::legislate();
        }
    }
}
fn main() {
    nation::government::govern();
}
