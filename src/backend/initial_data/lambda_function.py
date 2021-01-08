import sys
import json
import logging
import config
import pymysql
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)
response = {}

try:
    conn = pymysql.connect(
		config.DB_HOST,
		user = config.DB_USER,
		passwd = config.DB_PASSWORD,
        db = config.DB_NAME,
        connect_timeout = 10
    )
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL.")
    logger.error(e)
    sys.exit(1)

logger.info("SUCCESS: Connection to MySQL succeeded.")
def lambda_handler(event, context):
    try:
        sqls = [
            "DROP TABLE IF EXISTS ITEM",
            "CREATE TABLE ITEM (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, NAME varchar(256) NOT NULL, PAGES int NOT NULL, AUTHOR varchar(256) NOT NULL);",
            "INSERT INTO ITEM (NAME, PAGES, AUTHOR) VALUES ('test2', 100, 'mike');",
            "INSERT INTO ITEM (NAME, PAGES, AUTHOR) VALUES ('test', 333, 'shelly');",
            "INSERT INTO ITEM (NAME, PAGES, AUTHOR) VALUES ('test22', 234, 'tom');"
        ]
        with conn.cursor() as cur:
            for sql in sqls:
                cur.execute(sql)
            cur.execute('SELECT * FROM ITEM')
            print(cur.fetchall())
    except Exception as e:
        logger.error("ERROR: Unexpected error: SQL Execution error.")
        logger.error(e)
    finally:
        conn.close()
