package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/gorilla/mux"
)

func getJSON(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	data, _ := ioutil.ReadFile("GETdata.json")
	fmt.Fprintf(w, string(data))
}

func getCALC(w http.ResponseWriter, r *http.Request) {
	x := 1.0
	pi := 1.0
	i := 2
	for i != 10000 {
		x *= -1
		pi += x / float64((2*i - 1))
		i++
	}
	pi *= 4
	fmt.Fprintf(w, strconv.FormatFloat(pi, 'f', 16, 32))
}

func getHTML(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html")
	data, _ := ioutil.ReadFile("index.html")
	fmt.Fprintf(w, string(data))
}

func postJSON(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	data, _ := ioutil.ReadFile("POSTdataGO.json")

	newData := struct {
		UserID string `json:"userID"`
		UsrPW  string `json:"userPW"`
		Name   string `json:"name"`
		Age    int    `json:"age"`
	}{}
	_ = json.NewDecoder(r.Body).Decode(&newData)
	temp, _ := json.MarshalIndent(newData, "", "\t")

	if len(data) == 0 {
		data = []byte{'[', ' '}
	} else {
		data = append(data[:len(data)-2], []byte{',', '\n', '\t'}...)
	}
	data = append(data, temp...)
	data = append(data, []byte{'\n', ']'}...)
	ioutil.WriteFile("POSTdataGO.json", data, os.FileMode(744))
}

func main() {

	router := mux.NewRouter()

	router.HandleFunc("/server-speed/json", nil).Methods("GET")
	router.HandleFunc("/json", getJSON).Methods("GET")
	router.HandleFunc("/server-speed/calc", nil).Methods("GET")
	router.HandleFunc("/calc", getCALC).Methods("GET")
	router.HandleFunc("/server-speed/html", nil).Methods("GET")
	router.HandleFunc("/html", getHTML).Methods("GET")

	router.HandleFunc("/server-speed/post", nil).Methods("POST")
	router.HandleFunc("/post", postJSON).Methods("POST")

	fmt.Println("Server on PORT", 8090)
	log.Fatal(http.ListenAndServe(":8090", router))
}
