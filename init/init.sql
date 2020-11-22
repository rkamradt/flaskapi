CREATE DATABASE IF NOT EXISTS winelist;
USE winelist;
CREATE TABLE IF NOT EXISTS wine_pairing
  (id INT AUTO_INCREMENT NOT NULL,
   wine VARCHAR(255) NOT NULL,
   wine_description VARCHAR(255) NOT NULL,
   cheese VARCHAR(255) NOT NULL,
   cheese_description VARCHAR(255) NOT NULL,
   pairing_notes VARCHAR(255) NOT NULL,
   PRIMARY KEY(id))
   DEFAULT CHARACTER SET utf8mb4
   COLLATE `utf8mb4_unicode_ci`
   ENGINE = InnoDB;

INSERT INTO wine_pairing (wine, wine_description, cheese, cheese_description, pairing_notes)
  VALUES('wine1', 'wine1description', 'cheese1', 'cheese1description', 'notes1'),
  ('wine2', 'wine2description', 'cheese2', 'cheese2description', 'notes2'),
  ('wine3', 'wine3description', 'cheese3', 'cheese3description', 'notes3');
