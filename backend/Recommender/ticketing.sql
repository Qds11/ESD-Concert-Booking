
drop database if exists halldata;

create database halldata;
use halldata;

CREATE TABLE IF NOT EXISTS hall (
hall_id int NOT NULL,
hall_plan TEXT,
hall_name TEXT,
concert_id int,
concert_date DATE,
cat1_avail int,
cat2_avail int,
cat3_avail int,
cat4_avail int,
cat5_avail int,
cat1_price DECIMAL(10,2),
cat2_price DECIMAL(10,2),
cat3_price DECIMAL(10,2),
cat4_price DECIMAL(10,2),
cat5_price DECIMAL(10,2),
PRIMARY KEY(concert_id)
);

INSERT INTO hall (hall_id,hall_plan,hall_name,concert_id,concert_date,cat1_avail,cat2_avail,cat3_avail,cat4_avail,cat5_avail,cat1_price,cat2_price,cat3_price,cat4_price,cat5_price) VALUES
(1,'../../src/assets/halls/seating_plan_2.jpg','Singapore Stadium',1, '2023-06-23', 1000, 2000, 500, 700, 800, 288, 288, 268, 228, 198),
(2,'../../src/assets/halls/f9f85ae0-fb2f-11eb-a641-4e23b81c2c33.jpg','Victoria Theatre', 2,'2023-10-15', 0, 500, 500, null, null, 50,30,20,null,null),
(1,'../../src/assets/halls/seating_plan_2.jpg','Singapore Stadium',3, '2023-09-29', 1000, 2000, 500, 700, 800, 188, 188, 168, 158, 88)


