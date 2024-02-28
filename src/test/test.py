import json
import unittest
from unittest.mock import patch

from main import Exec


class TestExec(unittest.TestCase):

    @patch("your_module.boto3.client")
    def test_exec_run(self, mock_boto3_client):
        # モックオブジェクトの設定
        mock_ssm = mock_boto3_client.return_value
        mock_ssm.put_parameter.return_value = {
            "ResponseMetadata": {"HTTPStatusCode": 200}
        }
        mock_dynamodb = mock_boto3_client.return_value
        mock_dynamodb.put_item.return_value = {
            "ResponseMetadata": {"HTTPStatusCode": 200}
        }

        # Execインスタンスの作成と実行
        exec_instance = Exec()
        event = {
            "Records": [{"body": json.dumps({"id": "123", "message": "Hello, World!"})}]
        }
        context = {}
        exec_instance.run(event, context)

        # put_parameterが期待通りに呼び出されたことを検証
        mock_ssm.put_parameter.assert_called_with(
            Name="my-parameter", Value="my-value", Type="String", Overwrite=True
        )

        # put_itemが期待通りに呼び出されたことを検証
        mock_dynamodb.put_item.assert_called_with(
            TableName="my-table",
            Item={"id": {"S": "123"}, "message": {"S": "Hello, World!"}},
        )


if __name__ == "__main__":
    unittest.main()
