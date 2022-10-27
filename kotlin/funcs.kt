package vars

fun main() {
    println("sum of 2 and 4 is ${sum(2, 4)}");
    println("4 minus 2 is ${sub(4, 2)}");
    no_return(5, 6) // It does not returns meaningful value
    no_return1(10, 3)
}

fun no_return(a: Int, b: Int): Unit {
    println("I give nothing back but sum of ${a} and ${b} is ${sum(a, b)}")
}

fun no_return1(a: Int, b: Int) { // : Unit can be omitted
    println("I give nothing back but ${a} minus ${b} is ${sub(a, b)}")
}

fun sum(a: Int, b: Int): Int {
    return a + b
}

fun sub(a: Int, b: Int) = a - b
