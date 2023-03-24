-- Drop database if exists
DROP DATABASE IF EXISTS seat_database;

-- Create database
CREATE DATABASE seat_database;
USE seat_database;

-- Create table for seats
CREATE TABLE IF NOT EXISTS seats (
  id INT AUTO_INCREMENT PRIMARY KEY,
  hall_id INT NOT NULL,
  seat_count INT NOT NULL,
  category VARCHAR(64) NOT NULL,
  seatnumber VARCHAR(64) NOT NULL
);

-- Insert sample data into the seats table
INSERT INTO seats (hall_id, seat_count, category, seatnumber) VALUES (1, 50, 'VIP', 'A1');
INSERT INTO seats (hall_id, seat_count, category, seatnumber) VALUES (1, 100, 'Regular', 'B1');
INSERT INTO seats (hall_id, seat_count, category, seatnumber) VALUES (2, 75, 'Regular', 'C1');
INSERT INTO seats (hall_id, seat_count, category, seatnumber) VALUES (2, 25, 'VIP', 'D1');