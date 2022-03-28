package app

type ErrorMessage struct {
	Message string `json:"message"`
}

type PatchAlbumRequest struct { 
	Title      *string  
	Artist     *string  
	Price      *float32    
}
