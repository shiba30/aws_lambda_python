#!/bin/bash

# SQSキューの作成
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name MyQueue

# DynamoDBテーブルの作成
aws --endpoint-url=http://localhost:4566 dynamodb create-table \
    --table-name MyTable \
    --attribute-definitions AttributeName=MessageId,AttributeType=S \
    --key-schema AttributeName=MessageId,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

# Lambda関数の作成
aws --endpoint-url=http://localhost:4566 lambda create-function \
    --function-name MyLambdaFunction \
    --runtime python3.8 \
    --role arn:aws:iam::000000000000:role/lambda-ex \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://my-deployment-package.zip

# SQSからLambdaへのイベントソースマッピングの作成
QUEUE_ARN=$(aws --endpoint-url=http://localhost:4566 sqs get-queue-attributes --queue-url http://localhost:4566/000000000000/MyQueue --attribute-names QueueArn --query Attributes.QueueArn --output text)
aws --endpoint-url=http://localhost:4566 lambda create-event-source-mapping \
    --function-name MyLambdaFunction \
    --event-source-arn $QUEUE_ARN \
    --enabled \
    --batch-size 1

# API GatewayのREST APIの作成
REST_API_ID=$(aws --endpoint-url=http://localhost:4566 apigateway create-rest-api --name 'MyAPI' --region us-east-1 --query 'id' --output text)
# ルートリソースIDの取得
PARENT_ID=$(aws --endpoint-url=http://localhost:4566 apigateway get-resources --rest-api-id $REST_API_ID --query 'items[?path==`/`].id' --output text)
# リソースの作成
RESOURCE_ID=$(aws --endpoint-url=http://localhost:4566 apigateway create-resource --rest-api-id $REST_API_ID --parent-id $PARENT_ID --path-part start --query 'id' --output text)
# POSTメソッドの追加
aws --endpoint-url=http://localhost:4566 apigateway put-method --rest-api-id $REST_API_ID --resource-id $RESOURCE_ID --http-method POST --authorization-type NONE


# Step Functionsのステートマシンの作成
aws --endpoint-url=http://localhost:4566 stepfunctions create-state-machine --name MyStateMachine \
--definition file://state_machine.json \
--role-arn arn:aws:iam::000000000000:role/dummy-role
