import json

import boto3


def lambda_handler(event, context):
    dynamodb = boto3.client("dynamodb", endpoint_url="http://localhost:4566")

    # SQSメッセージからデータを取得
    for record in event["Records"]:
        message_body = record["body"]
        print(f"Processing message: {message_body}")

        # DynamoDBにデータを保存
        dynamodb.put_item(
            TableName="MyTable",
            Item={
                "MessageId": {"S": record["messageId"]},
                "MessageBody": {"S": message_body},
            },
        )

    return {"statusCode": 200, "body": json.dumps("Successfully processed!")}
