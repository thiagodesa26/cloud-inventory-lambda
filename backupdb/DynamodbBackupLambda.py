import boto3

client = boto3.client('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info('Function:{} has started'.format(context.function_name))
    client.create_backup(
        TableName='inventory',
        BackupName='MyAutomaticBackup'
    )
