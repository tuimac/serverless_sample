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
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM ITEM')
            rows = cur.fetchall()
            response['data'] = []
            for row in rows:
                response['data'].append(row)
        conn.commit()
        logger.info(response)
        return response
    except Exception as e:
        logger.error("ERROR: Unexpected error: SQL Execution error.")
        logger.error(e)
    finally:
        conn.close()
        logger.info("SUCCESS: Closing connection to MySQL succeeded.")
