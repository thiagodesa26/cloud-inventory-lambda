import json


def lambda_handler(event, context):
    # Mock Return
    return {
        'statusCode': 200,
        'body': json.dumps('Payment Received!')
    }
