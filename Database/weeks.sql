
CREATE DATABASE life__in_weeks;
USE life__in_weeks;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birthdate DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    category VARCHAR(50) DEFAULT 'personal',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
