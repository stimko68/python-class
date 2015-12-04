DROP DATABASE IF EXISTS star_wars;
CREATE DATABASE IF NOT EXISTS star_wars;
USE star_wars;

CREATE TABLE IF NOT EXISTS race (
  id INT AUTO_INCREMENT,
  race_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS player (
  id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  race_fk INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (race_fk) REFERENCES race (id)
);

CREATE TABLE IF NOT EXISTS ship (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ship_crew (
  id INT AUTO_INCREMENT,
  ship_fk INT NOT NULL,
  player_fk INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (player_fk) REFERENCES player (id),
  FOREIGN KEY (ship_fk) REFERENCES ship (id)
);

/* Seed data */
INSERT INTO race SET race_name = 'Droid';
INSERT INTO race SET race_name = 'Human';
INSERT INTO race SET race_name = 'Wookie';

INSERT INTO player SET name = 'C3PO', race_fk = 1;
INSERT INTO player SET name = 'R2D2', race_fk = 1;
INSERT INTO player SET name = 'Han Solo', race_fk = 2;
INSERT INTO player SET name = 'Chewbacca', race_fk = 3;
INSERT INTO player SET name = 'Darth Vader', race_fk = 2;
INSERT INTO player SET name = 'Emperor Palpatine', race_fk = 2;

INSERT INTO ship SET name = 'Millenium Falcon';
INSERT INTO ship SET name = 'Death Star';

INSERT INTO ship_crew SET ship_fk = 1, player_fk = 1;
INSERT INTO ship_crew SET ship_fk = 1, player_fk = 2;
INSERT INTO ship_crew SET ship_fk = 1, player_fk = 3;
INSERT INTO ship_crew SET ship_fk = 1, player_fk = 4;
INSERT INTO ship_crew SET ship_fk = 2, player_fk = 5;
INSERT INTO ship_crew SET ship_fk = 2, player_fk = 6;