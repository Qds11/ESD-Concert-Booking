


-- for local db
drop database if exists queue_database;

create database queue_database;
use queue_database;


-- for hosted db
-- USE sql12606226;

CREATE TABLE IF NOT EXISTS queue (
  id INT AUTO_INCREMENT PRIMARY KEY,
  concert_id INT NOT NULL,
  status ENUM('waiting', 'serving') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO queue (concert_id,status) VALUES (1,'serving');
INSERT INTO queue (concert_id,status) VALUES (1,'serving');
INSERT INTO queue (concert_id,status) VALUES (1,'serving');
INSERT INTO queue (concert_id,status) VALUES (1,'serving');
INSERT INTO queue (concert_id,status) VALUES (2,'serving');
INSERT INTO queue (concert_id,status) VALUES (2,'serving');
