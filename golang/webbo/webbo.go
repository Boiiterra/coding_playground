package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

const PORT string = ":6969"

type Dude struct {
	A int
	B bool
}

var served int = 0
var data []Dude

func main() {
	fmt.Println("Server available at:")
	fmt.Println(fmt.Sprintf("http://localhost%s", PORT))

	fmt.Println("To kill server:")
	fmt.Println("CTRL+c")
	fmt.Println()

	http.HandleFunc("/", core)
	http.HandleFunc("/api", handle)

	log.Println("Starting server...")
	err := http.ListenAndServe(PORT, nil)
	if err != nil {
		log.Println("That's bad.")
	}

}

func core(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, fmt.Sprintf("Served %d times.", served))
}

func handle(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		drop(w, r)
	case http.MethodPost:
		catch(w, r)
	default:
		http.Error(w, "That's illegal. Sorry can't do that.", http.StatusMethodNotAllowed)
	}
}

func drop(w http.ResponseWriter, _ *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization")

	w.Write([]byte(fmt.Sprintf("Served %d", served)))
	log.Println(fmt.Sprintf("Got some dudes. no.%d", served))
	served = served + 1
}

func catch(w http.ResponseWriter, r *http.Request) {
	var nt Dude

	if err := json.NewDecoder(r.Body).Decode(&nt); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	served = served + 1

	data = append(data, nt)
	log.Println(fmt.Sprintf("New dude's data added. no.%d", served))
}
