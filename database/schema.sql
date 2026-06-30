CREATE DATABASE accident_db;
USE accident_db;

CREATE TABLE accident_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    speed INT,
    weather VARCHAR(50),
    road_condition VARCHAR(50),
    vehicles INT,
    prediction VARCHAR(50),
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);