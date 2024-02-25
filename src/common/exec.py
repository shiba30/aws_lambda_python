from src.common.base import Base
import json


class Exec(Base):
    def __init__(self):
        super().__init__("Exec")

    def run(self, event, context):
        self.log(2, "Hello, World!")

        params = self.ssm.put_parameter(
            Name="my-parameter",
            Value="my-value",
            Type="String",
            Overwrite=True,
        )
        print(params)

        for event in event["Records"]:
            message = json.loads(event["body"])
            self.log("I", message)

            self.dynamodb.put_item(
                TableName="my-table",
                Item={
                    "id": {"S": message["id"]},
                    "message": {"S": message["message"]},
                },
            )

        return
