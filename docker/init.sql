USE Shop;

CREATE TABLE ITEM (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY
    TITLE varchar(255)
    AUTHOR varchar(255)
    PAGES int

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO ITEM (TITLE, AUTHOR, PAGES) values('When Breath Becomes Air', 'Paul Kalanithi', 100)
INSERT INTO ITEM (TITLE, AUTHOR, PAGES) values('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 200)
INSERT INTO ITEM (TITLE, AUTHOR, PAGES) values('Into Thin Air: A Personal Account of the Mt. Everest Disaster', 'Jon Krakauer', 121)
