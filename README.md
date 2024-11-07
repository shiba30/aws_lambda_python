# notification_delivery_by_aws

AWS Lambda（Python）を用いて、各サービス連携処理を行う

## Dockerfile の起動

docker build -t python_image .

docker run -d --name python_container python_image

## AWS サービスを LocalStack を使用して、開発とテスト用に作成

### 前提条件

Python と AWS CLI がインストールされていること。
LocalStack が Docker Compose を使って起動していること。

### ファイル構成

lambda_function.py: Lambda 関数のコード。
setup_resources.sh: 必要な AWS リソースをセットアップするスクリプト。

```
zip my-deployment-package.zip lambda_function.py
```

1. LocalStack を起動します。`docker-compose up`
2. setup_resources.sh スクリプトを実行して AWS リソースをセットアップします。
3. SQS キューにメッセージを送信し、Lambda 関数による処理と DynamoDB への記録をテストします。
