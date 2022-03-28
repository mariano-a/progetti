package app

import (
	"database/sql"
	"fmt"
	"log"
)

type HandlerDB struct {
	db *sql.DB
}
//hd.db
//func (hd *HandlerDB)connectToDB(config Config) error
func (hd *HandlerDB)ConnectToDB(config Config) (error) {
	var (
		db  *sql.DB
		err error
	)

	for {
		db, err = sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s:%s)/%s",
			config.Username,
			config.Password,
			config.Host,
			config.Port,
			config.Database,
		))
		if err != nil {
			log.Fatal(err)
		}

		err = db.Ping()
		if err == nil {
			break
		}
	}

	hd.db = db
	return nil
}

// albumsByArtist queries for albums that have the specified artist name.
func (hd *HandlerDB) albumsByArtist(name string) ([]Album, error) {
	// An albums slice to hold data from returned rows.
	var albums []Album

	rows, err := hd.db.Query("SELECT * FROM album WHERE artist = ?", name)
	if err != nil {
		return nil, fmt.Errorf("albumsByArtist %q: %v", name, err)
	}
	defer rows.Close()
	// Loop through rows, using Scan to assign column data to struct fields.
	for rows.Next() {
		var alb Album
		if err := rows.Scan(&alb.ID, &alb.Title, &alb.Artist, &alb.Price); err != nil {
			return nil, fmt.Errorf("albumsByArtist %q: %v", name, err)
		}
		albums = append(albums, alb)
	}
	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("albumsByArtist %q: %v", name, err)
	}
	return albums, nil
}

// albumByID queries for the album with the specified ID.
func (hd *HandlerDB) albumByID(id int64) (Album, error) {
	// An album to hold data from the returned row.
	var alb Album

	row := hd.db.QueryRow("SELECT * FROM album WHERE id = ?", id)
	if err := row.Scan(&alb.ID, &alb.Title, &alb.Artist, &alb.Price); err != nil { //Scan assegna i valori delle colonne di ciascuna riga ai campi della struttura dell'album.
		if err == sql.ErrNoRows {
			return alb, fmt.Errorf("albumsById %d: no such album", id)
		}
		return alb, fmt.Errorf("albumsById %d: %v", id, err)
	}
	return alb, nil
}

// addAlbum adds the specified album to the database,
// returning the album ID of the new entry
func (hd *HandlerDB) addAlbum(alb Album) (int64, error) {
	result, err := hd.db.Exec("INSERT INTO album (title, artist, price) VALUES (?, ?, ?)", alb.Title, alb.Artist, alb.Price) //Use DB.Exec to execute an INSERT statement.
	if err != nil {
		return 0, fmt.Errorf("addAlbum: %v", err)
	}
	id, err := result.LastInsertId() //Recupera l'ID della riga inserita nel database
	if err != nil {
		return 0, fmt.Errorf("addAlbum: %v", err)
	}
	return id, nil
}

	/*MAIN
	//QUERY FOR MULTIPLE ROW
	albums, err = handler.albumsByArtist("John Coltrane")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Albums found: %v\n", albums)

	//QUERY FOR A SINGLE ROW
	// Hard-code ID 2 here to test the query.
	alb, err := handler.albumByID(2)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Album found: %v\n", alb)

	//ADD A NEW ROW
	albID, err := handler.addAlbum(Album{
		Title:  "The Modern Sound of Betty Carter",
		Artist: "Betty Carter",
		Price:  49.99,
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("ID of added album: %v\n", albID)*/