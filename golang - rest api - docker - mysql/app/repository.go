package app

import (
	"database/sql"
	"fmt"
	//"encoding/json"
	//"io/ioutil"
	//"github.com/gorilla/mux"
	"strings"
)

func getAlbumsAll(hd *HandlerDB) ([]Album, error) {

	var albums []Album
	rows, err := hd.db.Query("SELECT id, title, artist, price FROM album WHERE is_disabled=0")
	if err != nil {
		return nil, fmt.Errorf("Error Query AlbumALL DB")
	}
	defer rows.Close()

	for rows.Next() {
		var album Album
		if err := rows.Scan(&album.ID, &album.Title, &album.Artist, &album.Price); err != nil {
			return nil, fmt.Errorf("Error Scan")
		}
		albums = append(albums, album)
	}

	if err = rows.Err(); err != nil {
		return nil, fmt.Errorf("Error")
	}
	return albums, nil
}

func getAlbumID(hd *HandlerDB, id string) (Album, error) {

	var album Album
	row := hd.db.QueryRow("SELECT * FROM album WHERE id = ? AND is_disabled = ?", id, false)

	err := row.Scan(&album.ID, &album.Title, &album.Artist, &album.Price, &album.IsDisabled)

	return album, err
}

func createAlbum(hd *HandlerDB, album Album) (int64, error) {
	//TODO return id just created
	var ins *sql.Stmt

	ins, err := hd.db.Prepare("INSERT INTO album (title, artist, price) VALUES (?, ?, ?)")
	defer ins.Close()

	result, err := ins.Exec(album.Title, album.Artist, album.Price)
	lastInsertedId, _ := result.LastInsertId()

	fmt.Println("ID of last row inserted: ", lastInsertedId)

	return lastInsertedId, err
	/*sqlStatement := "INSERT INTO album (title, artist, price) VALUES (?, ?, ?)"

	_, err := hd.db.Exec(sqlStatement, album.Title, album.Artist, album.Price)
	*/

}

func updateAlbum(hd *HandlerDB, album Album, id string) error {
	sqlStatement := "UPDATE album SET title=?, artist=?, price=? WHERE id=?"

	_, err := hd.db.Exec(sqlStatement, album.Title, album.Artist, album.Price, id)

	return err
}

func updatePatchAlbum(hd *HandlerDB, id int64, patchAlbum PatchAlbumRequest) (Album, error) {

	formatSqlStatement := []string{}
	value := []interface{}{}

	if patchAlbum.Title != nil {

		formatSqlStatement = append(formatSqlStatement, "title=?")
		value = append(value, *patchAlbum.Title)

	}
	if patchAlbum.Artist != nil {

		formatSqlStatement = append(formatSqlStatement, "artist=?")
		value = append(value, *patchAlbum.Artist)

	}
	if patchAlbum.Price != nil {

		formatSqlStatement = append(formatSqlStatement, "price=?")
		value = append(value, *patchAlbum.Price)

	}
	//sqlStatement := "UPDATE album SET " + strings.Join(formatSqlStatement, ", ") + " WHERE id=?"

	sqlStatement := fmt.Sprintf("UPDATE album SET %s WHERE id=?", strings.Join(formatSqlStatement, ", "))
	fmt.Println(sqlStatement)
	fmt.Println("type interface: ", value)

	var album Album
	if len(value) > 0 {
		value = append(value, id)
		_, err := hd.db.Exec(sqlStatement, value...)

		row := hd.db.QueryRow("SELECT * FROM album WHERE id = ? AND is_disabled = ?", id, false)

		err = row.Scan(&album.ID, &album.Title, &album.Artist, &album.Price, &album.IsDisabled)
		return album, err
	}

	return album, nil
	/*
		sqlStatement := `UPDATE album SET title=?, artist=?, price=? WHERE id=?`
		_, err := hd.db.Exec(sqlStatement, id)

		var ins *sql.Stmt

		ins, err := hd.db.Prepare("UPDATE album SET title=?, artist=?, price=? WHERE id=?")
		defer ins.Close()

		_, err := ins.Exec(album.Title, album.Artist, album.Price, id)

	*/
}

func deleteAlbum(hd *HandlerDB, id string) error {

	sqlStatement := "DELETE FROM album WHERE id=?"

	_, err := hd.db.Exec(sqlStatement, id)

	return err
}

func deleteAlbumSoft(hd *HandlerDB, id string) error {
	sqlStatement := "UPDATE album SET is_disabled=1 WHERE id=?"

	_, err := hd.db.Exec(sqlStatement, id)

	return err
}

/*'Il caffè della Peppina', 'Cristina D'Avena', '78.9'
 */
