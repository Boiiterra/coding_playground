package guess_num


fun randInt(): Int = (1..100).random()


fun main() {
    while (true) {
        var num = randInt()
        println("\n\nTry to guess number between 1 and 100 including both itegers")
        println("Or enter 0 to exit.")
        while (true) {
            print("Your guess: ")
            var guess = readln().toIntOrNull()
            if (guess is Int) {
                when {
                    guess > num -> println("Your guess is to big")
                    guess < num -> println("Your guess is to small")
                    guess == num -> {
                        println("\nYou guessed the number. It was $num")
                        break
                    }
                }
            }
        }
    }
}
