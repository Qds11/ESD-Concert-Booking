
-- for local db
drop database if exists queue_database;

create database queue_database;
use queue_database;


-- for hosted db
-- USE sql12606226;

CREATE TABLE IF NOT EXISTS queue (
  user_id INT NOT NULL,
  concert_id INT NOT NULL,
  status ENUM('waiting', 'serving') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, concert_id)
);

-- INSERT INTO queue (concert_id,status) VALUES (1,'serving');
-- INSERT INTO queue (concert_id,status) VALUES (1,'serving');
-- INSERT INTO queue (concert_id,status) VALUES (1,'serving');
-- INSERT INTO queue (concert_id,status) VALUES (1,'serving');
-- INSERT INTO queue (concert_id,status) VALUES (2,'serving');
-- INSERT INTO queue (concert_id,status) VALUES (2,'serving');
<<<<<<< HEAD

=======
>>>>>>> 427988ba79e35476a6da32315e1d37ca787f66de
DELIMITER $$
CREATE TRIGGER delete_serving_rows
BEFORE UPDATE ON queue
FOR EACH ROW
BEGIN
    IF NEW.status = 'serving' AND TIMESTAMPDIFF(MINUTE, NEW.created_at, NOW()) >= 11 THEN
        DELETE FROM queue WHERE user_id = NEW.user_id AND concert_id = NEW.concert_id;
    END IF;
<<<<<<< HEAD
END$$
DELIMITER ;

=======
END $$
DELIMITER;
>>>>>>> 427988ba79e35476a6da32315e1d37ca787f66de
