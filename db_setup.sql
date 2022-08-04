CREATE TABLE IF NOT EXISTS models (
	model_id INTEGER NOT NULL PRIMARY KEY,
	name VARCHAR(76) NOT NULL,
	likes INTEGER NOT NULL,
	slug TEXT, 
	uri TEXT, 
	image_uri TEXT,
	last_update TIMESTAMP NOT NULL,
	date_added TIMESTAMP NOT NULL DEFAULT (now() at time zone 'utc'));