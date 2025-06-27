import json
import boto3
import time

dynamodb = boto3.resource("dynamodb")
product_table = dynamodb.Table('Product')

def lambda_handler(event, ctx):
    if event['operation'] == 'addProduct':
        return saveProduct(event)
    else:
        return getProducts()


# TODO: Remove whitespace from json to make this function idiot-proof
def saveProduct(event: dict):
    gmt_time = time.gmtime()
    time_now = time.strftime('%a, %d %b %Y %H:%M:%S', gmt_time)
    product_table.put_item(
        Item={
            'productCode': event.get('productCode'),
            'price': event['price'],
            'createdAt': time_now
        }
    )

    return {
        'status_code': 200,
        'body': json.dumps(f"Product with ProductCode : {event.get('productCode')} created at {time_now}")
    }


def getProducts():
    response = product_table.scan()
    
    items = response['Items']
    print(items)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {
            'Content-Type': 'application/json',
        }
    } 
