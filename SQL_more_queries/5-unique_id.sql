-- script that created a  table with a unique id contraint
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
)