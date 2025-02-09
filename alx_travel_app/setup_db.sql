-- DB
CREATE DATABASE IF NOT EXISTS alx_travel_db;

-- USER
CREATE USER IF NOT EXISTS 'alx_user'@'localhost' IDENTIFIED BY 'testgg44';
GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'alx_user'@'localhost';

FLUSH PRIVILEGES;
