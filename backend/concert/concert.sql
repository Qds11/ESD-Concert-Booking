
-- for hosted db
-- USE sql12606226;

-- CREATE TABLE IF NOT EXISTS concert (
-- concert_id int NOT NULL AUTO_INCREMENT,
-- date_time DATETIME,
-- artist TEXT,
-- concert_name TEXT,
-- price DECIMAL(10,2),
-- hall_id int,
-- ticket_sale_date_time DATETIME,
-- description TEXT,
-- image_path TEXT,
-- PRIMARY KEY(concert_id)
-- );

-- INSERT INTO concert (date_time, artist, concert_name, price, hall_id, ticket_sale_date_time,description,image_path) VALUES
-- ('2023-06-23T19:30:00','txt','TXT Sweet Mirage Tour 2023' ,168.00,1,'2023-03-20T14:30:00','Hottest 4th Gen Kpop Group Finally in Singapore!','concert1.jpg'),
-- ('2023-10-15T19:00:00','Mr Cho','Cho Sweet Strings' ,50.00,1,'2023-05-20T14:30:00','Listen to the beautiful violin melodies by the classic Mr Cho','concert2.jpg'),
-- ('2023-09-29T19:00:00','Lil Pip','Pip Install FTW' ,90.00,2,'2023-07-20T14:30:00','Come listen to aggressive rap about python at its finest.','concert3.jpg');


-- for local db
drop database if exists concertdata;

create database concertdata;
use concertdata;

CREATE TABLE IF NOT EXISTS concert (
concert_id int NOT NULL AUTO_INCREMENT,
date_time DATETIME,
artist TEXT,
concert_name TEXT,
price DECIMAL(10,2),
hall_id int,
ticket_sale_date_time DATETIME,
description TEXT,
image_path TEXT,
genre TEXT,
status TEXT,
PRIMARY KEY(concert_id)
);

INSERT INTO concert (date_time, artist, concert_name, price, hall_id, ticket_sale_date_time,description,image_path,genre,status) VALUES
('2023-06-23T19:30:00','txt','TXT Sweet Mirage Tour 2023' ,168.00,1,'2023-03-20T14:30:00','Hottest 4th Gen Kpop Group Finally in Singapore!','concert1.jpg','K-POP','Concert sold out'),
('2023-10-15T19:00:00','Mr Cho','Cho Sweet Strings' ,50.00,1,'2023-05-20T14:30:00','Listen to the beautiful violin melodies by the classic Mr Cho','concert2.jpg','Classical','Concert available'),
('2023-09-29T19:00:00','Lil Pip','Pip Install FTW' ,90.00,2,'2023-07-20T14:30:00','Come listen to aggressive rap about python at its finest.','concert3.jpg','Rap','Concert available'),
('2023-11-05T20:00:00','Queen Tribute Band','We Will Rock You: A Tribute to Queen' ,60.00,3,'2023-08-20T14:30:00','Experience the magic of Queen and their iconic music','concert4.jpg','Rock','Concert available'),
('2023-12-10T18:00:00','The Nutcracker Ballet','The Nutcracker: A Holiday Ballet' ,80.00,2,'2023-09-15T14:30:00','A timeless classic ballet for the holiday season.','concert5.jpg','Ballet','Concert available'),
('2023-11-25T21:00:00','DJ IAmTheParty','IAmTheParty: Electronic Music' ,30.00,4,'2023-10-20T14:30:00','Get ready to dance to the hottest electronic beats of DJ IAmTheParty','concert6.jpg','Electronic','Concert available'),
('2022-12-31T23:59:59','The New Years Band','New Years Eve Concert' ,100.00,1,'2022-10-31T14:30:00','Celebrate the New Year with us and enjoy an evening of great music and fun!','concert7.jpg','Pop','closed'),
('2022-10-01T19:00:00', 'The Beatles', 'Revolutionary Sounds', 75.00, 2, '2022-09-01T14:00:00', 'Relive the magic of the Fab Four with this tribute band!', 'concert8.jpg', 'Rock', 'Concert available');


DELIMITER $$
CREATE TRIGGER concert_status_closed
AFTER INSERT ON concert
FOR EACH ROW
BEGIN
  IF NEW.date_time < NOW() THEN
    UPDATE concert SET status = 'closed' WHERE concert_id = NEW.concert_id;
  END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER delete_concert
BEFORE INSERT ON concert
FOR EACH ROW
BEGIN
    IF DATE_ADD(NEW.date_time, INTERVAL 7 DAY) <= NOW() THEN
        DELETE FROM concert WHERE concert_id = NEW.concert_id;
    END IF;
END $$
DELIMITER ;