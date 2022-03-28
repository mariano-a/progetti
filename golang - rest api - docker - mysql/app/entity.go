package app

type Album struct {
	ID         int64   `json:"id"`
	Title      string  `json:"title"`
	Artist     string  `json:"artist"`
	Price      float32 `json:"price"`
	IsDisabled bool    `json:"is_disabled,omitempty" sql:"is_disabled"`
}

type Config struct {
	Username string `json:"username"`
	Password string `json:"password"`
	Host     string `json:"host"`
	Port     string `json:"port"`
	Database string `json:"database"`
}


