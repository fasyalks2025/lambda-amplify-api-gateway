import json
import boto3
import time
from extra_type import DynamoDBTableLike, Operations

def lambda_handler(event: dict, ctx):
    dynamodb = boto3.resource("dynamodb")
    product_table = dynamodb.Table('Product')

    try:
        # Remove whitespace from event json to make this function idiot-proof
        operation: str = str(event.get('operation')).replace("", "")
    except Exception as e:
        return f"<stupid python: {e}>"

    if operation == Operations.addProduct:
        return saveProduct(event, product_table)

    if operation == Operations.listProducts:
        return getProducts(product_table)

    return {
        'status_code': 404,
        'body': json.dumps({"msg": "Operation does not exist"})
    }


def saveProduct(event: dict, table: DynamoDBTableLike):
    gmt_time = time.gmtime()
    time_now = time.strftime('%a, %d %b %Y %H:%M:%S', gmt_time)
    table.put_item(
        Item={
            'productCode': event.get('productCode'),
            'price': event.get('price'),
            'createdAt': time_now
        }
    )

    return {
        'status_code': 200,
        'body': json.dumps(f"Product with ProductCode : {event.get('productCode')} created at {time_now}")
    }


def getProducts(table: DynamoDBTableLike):
    response = table.scan()
    
    items = response['Items']
    print(items)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {
            'Content-Type': 'application/json',
        }
    } 

