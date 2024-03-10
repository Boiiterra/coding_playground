package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

const PORT string = ":6969"

func SomeMore(w http.ResponseWriter, r *http.Request) {
	html := `
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Testing server page</title>
            <style>
                * {
                    background-color: #232345;
                    color: #87675F;
                }

                a {
                    font-size: 10em;
                }
            </style>
        </head>
        <body>
            <div>
                <h1>Hello there bud</h1>
                <h2>This is all you are going to see bro.</h2>
                <h3>Stay hydrated. Eat well. Have a rest. Love you!</h3>
                <br>
                    <a href="..">back</a>
            </div>
        </body>
    </html>
    `

	fmt.Fprintf(w, html)
}

func Core(w http.ResponseWriter, r *http.Request) {
	var msg string
	file, err := os.Open("core.html")
	if err != nil {
		log.Fatal(err)
		msg = "This doesn't look good.\nThere is error in the code pls fix."
	}
	defer func() {
		if err = file.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	b, err := io.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	} else {
		msg = string(b)
	}

	fmt.Fprintf(w, msg)
}

func main() {
	log.Println("Hello, I am simplest web server imaginable.")

	http.HandleFunc("/", Core)
	http.HandleFunc("/extra", SomeMore)

	log.Println("Let's get started!")
	log.Println("Server is available at: http://localhost:6969")
	fmt.Println("To shut this bad boy off you must kill it with:\nCTRL+c")

	err := http.ListenAndServe(PORT, nil)
	if err != nil {
		log.Fatal(err)
	}
}
