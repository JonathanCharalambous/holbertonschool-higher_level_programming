-- script to create the force_name table
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
) ENGINE=INNODB;