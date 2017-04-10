package main

import (
	"fmt"
	"os"
	"encoding/json"
	"github.com/parnurzeal/gorequest"
	"github.com/robfig/cron"
)

type Configuration struct {
	Domain   string
}

func req() {
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
	request := gorequest.New()
	request.Get(configuration.Domain).End()
}

func main() {
	c := cron.New()
	c.AddFunc("@every 8m", req)
	c.Start()
	select {}

}
