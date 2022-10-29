package classes

/* I am a block of comments.
   Yea I like this feature.
   It is awesome. */

val PI = 3.14

open class Shape // Enpty class

class Circle(radius: Double): Shape() { // : Shape() <-- Inheritance between classes
    var diameter = radius * 2
    var area = PI * radius * radius
    var length = PI * diameter
}

fun main() {
    var circle = Circle(5.0)
    println(circle.diameter)
}