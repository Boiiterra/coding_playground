package loops

fun main() {
    val items = listOf("Apple", "Phone", "Banana", "Pineapple", "Watermelon")

    for (item in items) {
        println("Item -> $item")
    }

    for (index in items.indices) {
        println("Item number ${index + 1} is ${items[index]}")
    }

    var index = 0

    while (index < items.size) {
        println("Item at index $index is ${items[index]}")
        index++
    }

    // Iterate over range
    for (i in 1..10) {
        print("$i, ")
    }
    println("11.")

    // Iterate over progression
    for (i in 1..10 step 2) {
        print("$i ")
    }
    println()

    // Iterate over progression
    for (i in 9 downTo 0 step 3) {
        print("$i ")
    }
    println()

}
