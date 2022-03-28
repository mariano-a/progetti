package app

import (
	"encoding/json"
	"fmt"

	//"io/ioutil"
	"net/http"
	//"database/sql"
	"github.com/gorilla/mux"
	//"github.com/fatih/structs"
	"strconv"
)

func HealthCheck(w http.ResponseWriter, r *http.Request) {
	//specify status code
	w.WriteHeader(http.StatusOK)

	//update response writer
	fmt.Fprintf(w, "API is up and running")
}

func (handlerDB *HandlerDB) GetAlbumsAll(w http.ResponseWriter, r *http.Request) {

	albums, err := getAlbumsAll(handlerDB)
	if err != nil {
		fmt.Println("Error Query All Album: ", err)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	//json.NewEncoder(w).Encode(albums)

	jsonResponse, err := json.Marshal(albums)
	if err != nil {
		fmt.Println("Error Marshal: ", err)
		return
	}

	//update response
	w.Write(jsonResponse)

}

func (handlerDB *HandlerDB) GetAlbumID(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	w.Header().Set("Content-Type", "application/json")

	album, err := getAlbumID(handlerDB, params["id"])
	if err != nil {
		w.WriteHeader(404)
		messageError := ErrorMessage{Message: "user not found"}
		json.NewEncoder(w).Encode(messageError)
	} else {
		json.NewEncoder(w).Encode(album)
	}

}

func (handlerDB *HandlerDB) CreateAlbum(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	
	var album Album
	err := json.NewDecoder(r.Body).Decode(&album)
	if err != nil {
		w.WriteHeader(400) //bad request
		messageError := ErrorMessage{Message: "incorrect syntax request"}
		json.NewEncoder(w).Encode(messageError)
		return
	}
	
	id ,err := createAlbum(handlerDB, album)
	if err != nil {
		w.WriteHeader(500) //internal server error
		messageError := ErrorMessage{Message: "request not exec from server"}
		json.NewEncoder(w).Encode(messageError)
		return
	}
	album.ID = id
	json.NewEncoder(w).Encode(album)
	

	/*if err != nil {
		fmt.Println("Error Exec Post: ", err)
		return
	}
	
	
	   	w.Header().Set("Content-Type","application/json")
	   	var album AlbumJSON
	   	//_ = json.NewDecoder(r.Body).Decode(&album)

	   	//if err := json.NewDecoder(r.Body).Decode(&album); err != nil {
	           fmt.Println(err)
	           http.Error(w, "Error decoidng response object", http.StatusBadRequest)
	           return
	       }

	   	if err := json.NewEncoder(w).Encode(&album); err != nil {
	           panic(err)
	       }
	   	album.ID = strconv.Itoa(idCounter+1) //rand.Intn(100000000) dopo fai con id progressivo
	   	albumsJSON = append(albumsJSON,album)
	   	json.NewEncoder(w).Encode(album)*/
}

func (handlerDB *HandlerDB) UpdateAlbum(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)

	var album Album
	
	err := json.NewDecoder(r.Body).Decode(&album)
	if err != nil {
		w.WriteHeader(400) //bad request
		messageError := ErrorMessage{Message: "incorrect syntax request"}
		json.NewEncoder(w).Encode(messageError)
		return
	}

	err = updateAlbum(handlerDB, album, params["id"])
	if err != nil {
		w.WriteHeader(500) //internal server error
		messageError := ErrorMessage{Message: "request not exec from server"}
		json.NewEncoder(w).Encode(messageError)
		return
	}
	var id string = params["id"]
	i, _ := strconv.Atoi(id)
	album.ID = int64(i)
	json.NewEncoder(w).Encode(album)
	

}

func (handlerDB *HandlerDB) UpdatePatchAlbum(w http.ResponseWriter, r *http.Request){
	params := mux.Vars(r)
	
	
	var patchAlbum PatchAlbumRequest
	//id, err := strconv.Atoi(params["id"])
	id, err := strconv.ParseInt(params["id"], 10, 64)
	if err != nil {
		w.WriteHeader(400) //bad request
		messageError := ErrorMessage{Message: "incorrect syntax request"}
		json.NewEncoder(w).Encode(messageError)
		return
	}

	err = json.NewDecoder(r.Body).Decode(&patchAlbum)
	if err != nil {
		w.WriteHeader(400) //bad request
		messageError := ErrorMessage{Message: "incorrect syntax request"}
		json.NewEncoder(w).Encode(messageError)
		return
	}
	
	
	fmt.Printf("val: %v ; type: %[1]T\n", id)
	fmt.Println(err)
	fmt.Println(id)
		
	fmt.Println(params["id"])
	
	var album Album
	album, err = updatePatchAlbum(handlerDB, id, patchAlbum)
	if err != nil {
		w.WriteHeader(500) //internal server error
		messageError := ErrorMessage{Message: "request not exec from server"}
		json.NewEncoder(w).Encode(messageError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(album)
	

}

func (handlerDB *HandlerDB) DeleteAlbums(w http.ResponseWriter, r *http.Request) {
	//w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)

	err := deleteAlbum(handlerDB, params["id"])
	if err != nil {
		w.WriteHeader(500) //internal server error
		messageError := ErrorMessage{Message: "request not exec from server"}
		json.NewEncoder(w).Encode(messageError)
		return
	}

}

func (handlerDB *HandlerDB) DeleteAlbumsSoft(w http.ResponseWriter, r *http.Request) {

	//w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)

	err := deleteAlbumSoft(handlerDB, params["id"])
	if err != nil {
		fmt.Println("Error Exec Delete Soft: ", err)
		return
	}

}

/*
func createAlbum(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Content-Type","application/josn")
	var album AlbumJSON
	//_ = json.NewDecoder(r.Body).Decode(&album)

	//if err := json.NewDecoder(r.Body).Decode(&album); err != nil {
        fmt.Println(err)
        http.Error(w, "Error decoidng response object", http.StatusBadRequest)
        return
    }

	if err := json.NewEncoder(w).Encode(&album); err != nil {
        panic(err)
    }
	album.ID = strconv.Itoa(idCounter+1) //rand.Intn(100000000) dopo fai con id progressivo
	albumsJSON = append(albumsJSON,album)
	json.NewEncoder(w).Encode(album)

}

func (handlerDB *HandlerDB)updateAlbum(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Content-Type","application/json")
	params := mux.Vars(r)

	for index, item := range albumsJSON{
		if item.ID == params["id"]{
			albumsJSON = append(albumsJSON[:index], albumsJSON[index+1:]...)
			var album AlbumJSON
			_ = json.NewDecoder(r.Body).Decode(&album)
			album.ID = params["id"]
			albumsJSON = append(albumsJSON,album)
			return
		}
	}
}
/*
func updateAlbum(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Content-Type","application/josn")
	params := mux.Vars(r)

	for index, item := range albumsJSON{
		if item.ID == params["id"]{
			albumsJSON = append(albumsJSON[:index], albumsJSON[index+1:]...)
			var album AlbumJSON
			_ = json.NewDecoder(r.Body).Decode(&album)
			album.ID = params["id"]
			albumsJSON = append(albumsJSON,album)
			return
		}
	}
}

func deleteAlbums(w http.ResponseWriter, r *http.Request){
	println("1")
	w.Header().Set("Content-Type","application/josn")
	params := mux.Vars(r)
	for index, item := range albumsJSON{

		//i, _ := strconv.Atoi(params["id"])
		//id := int64(i)
		if item.ID == params["id"]{
			albumsJSON = append(albumsJSON[:index], albumsJSON[index+1:]...) //[4 5 6] append(4,6)
			break
		}
	}
	json.NewEncoder(w).Encode(albumsJSON)
}
*/
