-- script to create a table with deafault value for id
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256) NOT NULL
)