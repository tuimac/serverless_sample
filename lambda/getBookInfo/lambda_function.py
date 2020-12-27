import json
import config

def lambda_handler(event, context):
    print(config.DB_NAME)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
