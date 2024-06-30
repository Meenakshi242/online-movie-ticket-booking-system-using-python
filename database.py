CREATE DATABASE project_2;

USE project_2;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movies VARCHAR(255),
    hall VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    charges int
);

CREATE TABLE Booking_Details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    movies VARCHAR(255),
    hall VARCHAR(255),
    time VARCHAR(255),
    date VARCHAR(255),
    charges_with_gst int,
    seat_num VARCHAR(255)
);

INSERT INTO movies (movies, hall, date, time, charges)
VALUES ('karudan', 'A', '24 june', '12.30pm', 250),
       ('rathnam', 'C', '24 june', '10.00pm', 200),
       ('star', 'B', '25 june', '4.00pm', 190),
       ('j baby', 'B', '26 june', '2.30pm', 250),
       ('Maharaja', 'C', '27 june', '10.30am', 200),
       ('rail', 'A', '27 june', '6.20pm', 280),
       ('dear', 'B', '28 june', '4.30pm', 230),
       ('kalki', 'C', '29 june', '2.00pm', 250),
       ('ranam', 'A', '30 june', '10.30am', 200),
       ('devil', 'B', '30 june', '6.00pm', 190);
