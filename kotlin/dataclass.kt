package dataclass

data class Cat(val name: String = "", var age: Int = 0) {
    var color: String = "White"
}

fun main() {
    val pinky = Cat("Pinky", 3)
    pinky.color = "Pink"
    var (name, age) = pinky
    println("My cat's name is $name and she is $age")

    val rosy = pinky.copy(name="Rosy")
    var (name1, age1) = rosy
    println("My other cat's name is $name1 and she is also $age1")

    if (pinky.equals(rosy)) {
        println("Pinky and Rosy are equal one to another.")
    } else {
        println("They are not equal.")
    }
}
