package main

import "fmt"

func Msg(name string) string {
	message := fmt.Sprintf("Hello, %v. How are you doing?", name)
    return message
}

func main() {
    fmt.Println(Msg("BOIIIS"));
}

