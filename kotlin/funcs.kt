package funcs

fun main() {
    println("sum of 2 and 4 is ${sum(2, 4)}");
    println("4 minus 2 is ${sub(4, 2)}");
    no_return(5, 6) // It does not returns meaningful value
    no_return1(10, 3)
    println(named(y = 5, z = 8, x = 9))
    println(default(5, 4))
    println(default(a = 4))
    println(default(b = 10))
    even(1)
    even(1, 54, 85, 64)
    even(1, 100, 45, 78, 98, 65, 56)
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

fun named(x: Int, y: Int, z: Int): List<Int> {
    return listOf(x, y, z)
}

fun default(a: Int = 1, b: Int = 1): Int = a * b

fun even(vararg nums: Int) {
    nums.forEach { num -> if (num % 2 == 0) println("$num is even") }
}