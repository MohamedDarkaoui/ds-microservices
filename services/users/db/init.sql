CREATE DATABASE users;

\connect users

CREATE TABLE users (
  username VARCHAR(250)  PRIMARY KEY,
  password VARCHAR(250) NOT NULL
);

CREATE TABLE friends (
  requester VARCHAR(250) REFERENCES users,
  addressee VARCHAR(250) REFERENCES users,
  PRIMARY KEY (requester, addressee)
);

CREATE TABLE groups (
  administrator VARCHAR(255) REFERENCES users,
  groupname VARCHAR(255) PRIMARY KEY
);

CREATE TABLE group_members (
  groupname VARCHAR(255) REFERENCES groups,
  member VARCHAR(255) REFERENCES users,
  PRIMARY KEY (groupname, member)
);