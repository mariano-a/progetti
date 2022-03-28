package main

import (
	 
	"encoding/json"
	"fmt"
	"log"
	"os"
	//"math/rand"
	_ "github.com/go-sql-driver/mysql"
	"net/http"

    //"github.com/gin-gonic/gin"
	//"gopkg.in/gorp.v1"
	//"strconv"
	"github.com/gorilla/mux"
	"docker/app"
	
)



func main() {

	fileContent, err := os.ReadFile("./config.json")
	if err != nil {
		log.Fatal(err)
	}
	
	var config app.Config
	err = json.Unmarshal(fileContent, &config)
	if err != nil {
		fmt.Println("Error JSON Unmarshalling")
		log.Fatal(err)
	}
	fmt.Println(config.Username, config.Port)
	

	handler := app.HandlerDB{}

	err = handler.ConnectToDB(config)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Connected!")

	router := mux.NewRouter()
	
	router.HandleFunc("/check/", app.HealthCheck).Methods(http.MethodGet)
	router.HandleFunc("/albums/", handler.GetAlbumsAll).Methods(http.MethodGet)
	router.HandleFunc("/albums/",handler.CreateAlbum).Methods(http.MethodPost)
	router.HandleFunc("/albums/{id}/",handler.GetAlbumID).Methods(http.MethodGet)
	router.HandleFunc("/albums/{id}/",handler.UpdateAlbum).Methods(http.MethodPut)

	router.HandleFunc("/albums/patch/{id}/",handler.UpdatePatchAlbum).Methods(http.MethodPatch)

	router.HandleFunc("/albums/{id}/", handler.DeleteAlbums).Methods(http.MethodDelete)
	router.HandleFunc("/albums/soft/{id}/", handler.DeleteAlbumsSoft).Methods(http.MethodDelete)
	
	fmt.Printf("Starting server at port 8080\n")
	log.Fatal(http.ListenAndServe(":8080",router))

}



