package string

fun main() {
    var any = 1235
    var str1 = "Any is $any"

    any = 8965
    var str2 = "${str1.replace("is", "was")}, but now it is $any."

    println("$str2")
}