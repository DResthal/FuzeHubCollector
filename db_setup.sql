CREATE TABLE IF NOT EXISTS models (
	id INTEGER NOT NULL PRIMARY KEY,
	name VARCHAR(76) NOT NULL,
	likes INTEGER NOT NULL,
	url TEXT,
	downloads INTEGER,
	last_update TIMESTAMP NOT NULL DEFAULT (now() at time zone 'utc'),
	date_added TIMESTAMP NOT NULL DEFAULT (now() at time zone 'utc'));