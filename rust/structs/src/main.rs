#![allow(unused)]

struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn is_bigger(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

impl Rectangle {
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let rect1: Rectangle = Rectangle { width: 45, height: 10 };
    let rect2: Rectangle = Rectangle { width: 12, height: 5 };

    println!("Area of the rect1 with width={} and height={} is equals to {}.",
             rect1.width, rect1.height, rect1.area());
    println!("Area of the rect2 with width={} and height={} is equals to {}.",
    rect2.width, rect2.height, rect2.area());

    println!("rect1 is bigger than rect2? {}", rect1.is_bigger(&rect2));
    println!("rect2 is bigger than rect1? {}", rect2.is_bigger(&rect1));

    // I am square
    let sqr = Rectangle::square(4);
    println!("I am square and can prove that: my width is {} and height is {}.",
             sqr.width, sqr.height);
    println!("And I occupy area that is equals to {}.", sqr.area())
}

struct Color(u8, u8, u8);

struct NoFields;

struct Book {
    name: String,
    pages: u32,
    author: String,
    color: Color
}

fn unused() {
    let fav_book: Book = Book {
        name: String::from("Favorite"),
        author: String::from("TerraBoii"), 
        pages: 1953,
        color: Color(0, 24, 56),
    };

    let one: NoFields = NoFields;
    let two: NoFields = NoFields;

    println!("My favorite book is \"{}\" it is written by {} and has {} pages. It's color is {}.",
             fav_book.name, fav_book.author, fav_book.pages, fav_book.color.0 + fav_book.color.1 + fav_book.color.2);
}
