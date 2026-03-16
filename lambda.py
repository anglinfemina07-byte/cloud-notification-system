import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):

    sns.publish(
        TopicArn='YOUR_TOPIC_ARN',
        Message='Cloud notification triggered',
        Subject='Notification'
    )

    return {
        'statusCode': 200,
        'body': 'Notification sent'
    }