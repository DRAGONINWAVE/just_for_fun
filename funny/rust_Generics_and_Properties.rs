fn max(array: &[i32]) -> i32 {
    let mut max_index = 0;
    let mut i = 1;
    while i < array.len() {
        if array[i] > array[max_index] {
            max_index = i;
        }
        i += 1;
    }
    array[max_index]
}
fn main() {
    let a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    println!("max = {}", max(&a));
}
