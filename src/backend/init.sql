use bookmanager;

CREATE TABLE ITEM (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NAME varchar(256) NOT NULL,
    PAGES int NOT NULL,
    AUTHOR varchar(256) NOT NULL
);
INSERT INTO ITEM (NAME, PAGES, AUTHOR) VALUES ('test2', 100, 'mike');
INSERT INTO ITEM (NAME, PAGES, AUTHOR) VALUES ('test', 333, 'shelly');
INSERT INTO ITEM (NAME, PAGES, AUTHOR) VALUES ('test22', 234, 'tom');
