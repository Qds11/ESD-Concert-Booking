-- USE sql12606226;


-- drop database if exists ticket_db;

drop database if exists users;


create database users;
use users;



CREATE TABLE IF NOT EXISTS user (
user_id int NOT NULL AUTO_INCREMENT,
username TEXT,
email TEXT,
contact int NOT NULL,
joined_date_time DATETIME,
birthdate DATE,
genre_preferred TEXT,
PRIMARY KEY(user_id)
);

INSERT INTO user (username, email, contact, joined_date_time, birthdate, genre_preferred) VALUES
('jigglypuff','teamjigglypuff335@gmail.com', 90628232,'2023-03-16T14:04:23' ,'2002-05-20','K-POP'),
('pikachu','pikachu123@gmail.com', 88181688,'2023-03-16T14:04:30' ,'2001-01-01','Classical'),
('snorlax','snorlax@hotmail.com', 99192939,'2023-03-16T13:18:28' ,'2002-01-30','Rap'),
('mew','mew@yahoo.com', 98981919,'2023-03-16T13:55:25' ,'2003-03-03','K-POP'),
('squirtle','squirtle@gmail.com', 84881748,'2023-03-16T12:04:23' ,'2007-10-11','Rap'),
('charmander','chare@gmail.com', 96281885,'2023-03-16T12:04:23' ,'1960-10-11','Classical'),
('charizard', 'xhihyuxxx@gmail.com', 96281884, '2023-04-01T13:19:55','1966-11-11','K-POP')

