package conditions

fun main() {
    val list = listOf("a", "B", "c")

    println(maxOf(5, 2))
    println(minOf(5, 2))
    case(1)
    case(6)
    println(describe("obj"))
    println(describe(2.0))
    println(describe(4545654654654))
    println(describe(5))
    in_range(5)
    in_range(-10, 5)

    if (-1 !in 0..list.lastIndex) {
        println("-1 is outside of range 0 to ${list.lastIndex}")
    }

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

fun in_range(x: Int, upper_lim: Int = 10) {
    if (x in 1..upper_lim) {
        println("Indeed in range")
    } else {
        println("Unfortunately not in range")
    }
}

fun describe(obj: Any): String = 
    when (obj) {
        is Int -> "Is integer"
        is Double -> "Is double"
        is Long -> "Is looooong"
        !is String -> "Is not a string"
        else -> "Unknown"
    }
