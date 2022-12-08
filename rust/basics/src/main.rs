fn main() {
    mut_();
    scopes();
    if_else();
    loops();
    while_();
    for_loops();
}


fn mut_() {
    let mut m = String::from("I am mutable");
    let i = String::from("I am immutable");

    println!("{i}");
    println!("{m} and can prove that:");

    m = String::from("See... I am mutable.");
    println!("{m}");
}


fn if_else() {
    let mut something = true;

    if something {
        something = !something;
        println!("Something was true and I printed this.");
    } else if !something {
        something = !something;
        println!("Something was false and I printed this.");
    }

    println!("Now something is {}", something)
}


fn scopes() {
    let mut x = 10;
    println!("This x is {x}");
    {
        let x = 2;
        println!("That x is {x}");
    }
    x += 1;
    println!("And finally x + 1 is {x}!")
}


fn numeric_ops() {
    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;
    let floored = 2 / 3; // Results in 0

    // remainder
    let remainder = 43 % 5;
}


fn loops() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}


fn while_() {
    let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");
}


fn for_loops() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}