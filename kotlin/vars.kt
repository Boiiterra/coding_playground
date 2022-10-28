package vars

val PI = 3.14
var x = 3

fun main() {
    // Constants values
    val str: String = "I am constant"
    val wow = "No need to type type"
    val later: String // Type required when no initializer is provided
    later = "I have value that was assigned later"

    // Variables
    var integer: Int = 23
    var hello = "Bonjour"

    // Output options
    println("Constant values:")
    println("Pi -> $PI")
    println("str -> $str")
    println("wow -> $wow")
    println("later -> $later")
    println("Variables:")
    println("integer -> $integer")
    println("hello -> $hello")
    println("x before increment -> $x")
    incrementX()
    println("x after increment -> $x")
    println("integer times 7 is ${integer * 7}")
}

fun incrementX() {
    x += 7
}