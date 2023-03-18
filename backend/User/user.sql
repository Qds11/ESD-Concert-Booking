USE sql12606226;

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
('jigglypuff','teamjigglypuff335@gmail.com', 97881010,'2023-03-16T14:04:23' ,'2002-05-20','K-POP'),
('pikachu','pikachu123@gmail.com', 88181688,'2023-03-16T14:04:30' ,'2001-01-01','Classical'),
('snorlax','snorlax@hotmail.com', 99192939,'2023-03-16T13:18:28' ,'2002-01-30','Rap'),
('mew','mew@yahoo.com', 98981919,'2023-03-16T13:55:25' ,'2003-03-03','K-POP'),
('squirtle','squirtle@gmail.com', 84881748,'2023-03-16T12:04:23' ,'2007-10-11','Rap'),

