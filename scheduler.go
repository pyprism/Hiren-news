package main

import (
	"fmt"
	//"io/ioutil"
	"os"
	"encoding/json"
)

type Configuration struct {
	consumer_key   string
	consumer_secret   string
	access_token   string
	access_token_secret   string
	db_name   string
	db_user   string
	db_password   string
	secret_key   string
	fb_page   string
	fb_page_token   string
	domain   string
}

func main() {
	//data, err := ioutil.ReadFile("./config.json")
	//if err != nil {
	//	fmt.Println(err)
	//	return
	//}
	file, err := os.Open("./config.json")
	if err != nil {
		fmt.Println(err)
		return
	}
	decoder := json.NewDecoder(file)
	configuration := Configuration{}
	error_ := decoder.Decode(&configuration)
	if error_ != nil {
		fmt.Println("error:", err)
		return
	}
	fmt.Println(configuration.domain)
	//fmt.Print("data:  ",string(data))
}
