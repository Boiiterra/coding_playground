package code.funny

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

fun main() {
	val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")
	val current = LocalDateTime.now().format(formatter)

	println(current.toString())
}
