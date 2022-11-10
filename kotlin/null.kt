package nullable

fun parseInt(arg: String): Int? { // <T>? <-- type is nullable 
    return arg.toIntOrNull()
}

fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)

    // Using `x * y` yields error because they may hold nulls.
    if (x != null && y != null) {
        // x and y are automatically cast to non-nullable after null check
        println(x * y)
    }
    else {
        println("'$arg1' or '$arg2' is not a number")
    }    
}

fun main() {
    printProduct("6", "7")
    printProduct("a", "7")
    printProduct("a", "b")

    var a: String? = "old"
    println("a is '$a'")
    a = null
    println("a is '$a' now")
    // Elvis operator
    val length = a?.length ?: -1
    println("a's length is $length")

    // !! -> throws NPE
    println("Now we are going to see how lucky you are.")
    val game: String? = if ((1..10).random() > 5) "Good job!!" else null
    var luck = game!!.length
    println("You got lucky. Luck code: $luck")
}
