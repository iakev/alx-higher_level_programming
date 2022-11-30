-- Gracefully creates a database 'hbtn_0d_usa' and gracefully adds 'states'
-- table with id (unique auto generated can't be null and is a pk)
-- table also contains name which can't be Null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
       id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
