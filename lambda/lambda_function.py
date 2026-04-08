# lambda_function.py

import json
import os

def lambda_handler(event, context):
    table_name = os.environ.get("TABLE_NAME")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Python Lambda",
            "table": table_name
        })
    }