import json
import boto3
import os
import decimal

sns = boto3.client('sns')


def lambda_handler(event, context):

    #    print("Got event: " + json.dumps(event))

    snsArn = os.environ['sns_arn']
    minQuantity = int(os.environ['min_item_quantity'])

    for record in event['Records']:
        if record['eventName'] != "MODIFY":
            continue

        newImage = record['dynamodb']['NewImage']
        if not 'Quantity' in newImage:
            continue

        productId = record['dynamodb']['Keys']['product_id']['S']
        newQuantity = newImage['Quantity']['N']

        print("Product: " + productId + " quantity changed to: " + newQuantity)

        if(int(newQuantity) <= minQuantity):
            print("sending message to: " + snsArn)

            message = "Item " + productId + " low quantity"

            response = sns.publish(
                TargetArn=snsArn,
                Message=json.dumps({
                    'default': json.dumps(message)

                }),
                MessageStructure='json'
            )
