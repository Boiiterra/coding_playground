// use std::fs::File;
// use std::io::ErrorKind;
use std::fs::{self, File};
use std::io::{self, Read, ErrorKind};

fn main() {

    _ = read_hello_file();
    _ = read_hello_file_short();
    _ = read_hello_file_even_shorter();
    _ = read_hello_file_the_shortest();

    let greeting_file_result = File::open("hello.txt");

    let _greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error);
            }
        },
    };

    let _greeting_file = File::open("Hello.txt").unwrap(); // panics on error
    let _greeting_file = File::open("Hello.txt")
        .expect("Hello.txt should be included in this project."); // panics too


}

// Propagating errors:

fn read_hello_file() -> Result<String, io::Error> {
    let hello_file_result = File::open("hello.txt");

    let mut hello_file = match hello_file_result {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut hello = String::new();
    
    match hello_file.read_to_string(&mut hello) {
        Ok(_) => Ok(hello),
        Err(e) => Err(e),
    }
}

fn read_hello_file_short() -> Result<String, io::Error> {
    let mut hello_file = File::open("hello.txt")?;
    let mut hello = String::new();
    hello_file.read_to_string(&mut hello)?;
    Ok(hello)
}

fn read_hello_file_even_shorter() -> Result<String, io::Error> {
    let mut hello = String::new();

    File::open("hello.txt")?.read_to_string(&mut hello)?;

    Ok(hello)
}

fn read_hello_file_the_shortest() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}

fn _last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}