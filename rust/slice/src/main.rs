fn main() {
    let mut s = String::from("This is string that I created.");
    let word = first_word(&s);
    let sliced = &s[..word];
    println!("First word of this string '{}' is:", s);
    println!("{}", sliced);
}

fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}
