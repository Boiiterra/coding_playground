package oop


fun main() {
    val joe = Person("Joe", "Brown", 30)
    val jane = Person("Jane", "Brown", 65, joe)
    println(jane.children[0].firstName)
    println()
    val one = SomeClass(154.0, 10.0)
    println(one.test)
    println(one.summ)
    println(one.sub())
    val two = SomeClass(14.0, 10.0)
    println(two.test)
}


class Person(val firstName: String, val lastName: String, val age: Int) {
    val children: MutableList<Person> = mutableListOf()

    init {
        println("$firstName $lastName is now in this virtual world.")
    }

    constructor(firstName: String, lastName: String, age: Int, child: Person): 
        this(firstName, lastName, age) {
            children.add(child)
    }

    // empty constructor]
    constructor(): this("", "", -1)
}


data class SomeClass(var arg1: Double, var arg2: Double) {
    var summ = arg1 + arg2

    var test = 1
        get() = field + 1
        set(value) {
            if (value < 0) println("Setted value is negative.")
            field = value
        }

    fun sub() = arg1 - arg2

}