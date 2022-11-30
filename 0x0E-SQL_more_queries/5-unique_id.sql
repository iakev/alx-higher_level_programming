-- Script that creates table 'unique_id' on Server with unique id and name value
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE, name VARCHAR(256)
);
