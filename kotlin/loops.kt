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

}
