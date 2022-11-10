package lambda

fun main() {
    val lst = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9)

    lst.forEach { it -> println(it) }
    println(lst.map { it -> it * 2 })
    println(lst.filter { it -> it % 2 == 1 })
    println(lst.reduce { sum, it -> sum + it }) // sum()

    println(lst.sortedByDescending { it })

    println(lst.any { it -> it > 10 })
    println(lst.all { it < 10 })

    println(lst.sum())

    val new = listOf(-1, 2, -10, -45, 86)
    val (positive, not_positive) = new.partition { it > 0 }

    println(positive)
    println(not_positive)

    val result = listOf("a", "b", "hello", "long", "tall").groupBy { it.length }
    println(result) // HashMap or LinkedHashMap
}