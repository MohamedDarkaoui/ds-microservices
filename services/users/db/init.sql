CREATE DATABASE users;
\connect users
CREATE TABLE users (
  username VARCHAR(250)  PRIMARY KEY,
  password VARCHAR(250) NOT NULL
);

INSERT INTO users VALUES ('a','a');