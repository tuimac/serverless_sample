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
            result = {}
            for row in rows:
                book = {}
                book['name'] = row[1]
                book['pages'] = row[2]
                book['author'] = row[3]
                result[row[0]] = book
        conn.commit()
        logger.info(result)
        response['statusCode'] = 200
        result['event'] = event
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"             
            },
            'body': json.dumps(result)
        }
    except Exception as e:
        logger.error("ERROR: Unexpected error: SQL Execution error.")
        logger.error(e)
    finally:
        #conn.close()
        logger.info("SUCCESS: Closing connection to MySQL succeeded.")
