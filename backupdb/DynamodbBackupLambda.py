import boto3

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    client.create_backup(
        TableName='inventory',
        BackupName='MyAutomaticBackup'
    )
