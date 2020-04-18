import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb')


def result(status, message):
    return {
        'statusCode': status,
        'body': message,
        'headers': {
            'Content-Type': 'application/json'
        }
    }


def lambda_handler(event, context):
    table = dynamodb.Table('inventory')
    itemId = event['pathParameters']['itemid']

    if event['httpMethod'] == 'GET':
        response = table.get_item(Key={'product_id': itemId})
        if 'Item' in response:
            item = response['Item']
        else:
            return result(400, 'item not found!')
    else:
        callBody = json.loads(event['body'])
        newQuantity = callBody['newQuantity']

        response = table.update_item(
            Key={
                'product_id': itemId
            },
            UpdateExpression="set Quantity=:q",
            ExpressionAttributeValues={
                ':q': int(newQuantity)
            },
            ReturnValues='ALL_NEW'
        )
        item = response['Attributes']

    item['Quantity'] = int(item['Quantity'])

    return result(200, json.dumps(item))
