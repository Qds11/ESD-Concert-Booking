

USE sql12606226;

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
PRIMARY KEY(concert_id)
);

INSERT INTO concert (date_time, artist, concert_name, price, hall_id, ticket_sale_date_time,description,image_path) VALUES
('2023-06-23T19:30:00','txt','TXT Sweet Mirage Tour 2023' ,168.00,1,'2023-03-20T14:30:00','Hottest 4th Gen Kpop Group Finally in Singapore!','concert1.jpg'),
('2023-10-15T19:00:00','Mr Cho','Cho Sweet Strings' ,50.00,1,'2023-05-20T14:30:00','Listen to the beautiful violin melodies by the classic Mr Cho','concert2.jpg'),
('2023-09-29T19:00:00','Lil Pip','Pip Install FTW' ,90.00,2,'2023-07-20T14:30:00','Come listen to aggressive rap about python at its finest.','concert3.jpg');

