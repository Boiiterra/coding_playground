package conditions

fun main() {
    println(maxOf(5, 2))
    println(minOf(5, 2))
    case(1)
    case(6)
}

fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}

fun minOf(a: Int, b: Int) = if (a < b) a else b

fun case(x: Int) {
    when (x) {
        1 -> println("x == 1")
        5 -> println("x == 5")
        else -> {
            println("x is neither 1 nor 5")
        }
    }
}