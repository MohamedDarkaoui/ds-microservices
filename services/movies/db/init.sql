CREATE DATABASE movies;

\connect movies

CREATE TABLE movies (
    Title TEXT PRIMARY KEY,
    Description TEXT,
    Year INT,
    Runtime INT
);

\copy movies FROM '/usr/src/app/movies.csv' DELIMITER ',' CSV HEADER