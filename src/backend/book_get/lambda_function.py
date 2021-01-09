import sys
import json
import logging
import config
import pymysql
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
        name = event['name']
        body = {}
        with conn.cursor() as cur:
            if name == '':
                cur.execute('SELECT * FROM ITEM')
            else:
                cur.execute('SELECT * FROM ITEM WHERE NAME=%s', (name))
            rows = cur.fetchall()
            booklist = []
            for row in rows:
                book = {}
                book['name'] = row[1]
                book['pages'] = row[2]
                book['author'] = row[3]
                booklist.append(book)
            body['result'] = booklist
        conn.commit()
        logger.info(body)
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"             
            },
            'body': json.dumps(body)
        }
    except Exception as e:
        logger.error("ERROR: Unexpected error: SQL Execution error.")
        traceback.print_exc()
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*"             
            },
            'body': json.dumps({'message': 'error'})
        }
