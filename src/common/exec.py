import json

from .base import Base


class Exec(Base):
    def __init__(self):
        super().__init__("Exec")

    def run(self, event=None, context=None):
        self.log(2, "Hello, World!")

        """
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
        """
        return
