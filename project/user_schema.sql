CREATE SCHEMA IF NOT EXISTS user_schema;
USE user_schema;

CREATE TABLE IF NOT EXISTS user (
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS itineraries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(255) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    hotel VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_email) REFERENCES user(email)
);

CREATE TABLE IF NOT EXISTS user_itinerary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    itinerary_id INT NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email),
    FOREIGN KEY (itinerary_id) REFERENCES itineraries(id)
);


CREATE TABLE IF NOT EXISTS itinerary_activity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    itinerary_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    phonenumber VARCHAR(20),
    cost FLOAT,
    cost_estimate VARCHAR(255),
    category VARCHAR(255),
    hours TEXT,
    isBreakfast BOOLEAN,
    isLunch BOOLEAN,
    isDinner BOOLEAN,
    rating FLOAT,
    website VARCHAR(255),
    FOREIGN KEY (itinerary_id) REFERENCES itineraries(id)
);



