package collect

fun main() {
    val fruits = listOf("apple", "banana", "kiwifruit", "avocado", "pineapple")

    // Iterate over collection
    for (fruit in fruits) {
        println(fruit)
    }

    when {
        "orange" in fruits -> println("Juicy")
        "apple" in fruits -> println("Apple is fine too")
    }

    fruits
        .filter { it.startsWith("a") }
        .sortedBy { it }
        .map { it.uppercase() }
        .forEach { println(it) }
}