import logging
from abc import ABC, abstractmethod

# import boto3


class Base(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.logger.addHandler(logging.StreamHandler())
        self.logger.handlers[0].setFormatter(self.formatter)
        # self.s3 = boto3.client("s3")
        # self.sns = boto3.client("sns")
        # self.sqs = boto3.client("sqs")
        # self.dynamodb = boto3.client("dynamodb")

    @abstractmethod
    def run(self):
        pass

    def log(self, id, message):
        if id == "E":
            self.logger.error(message)
        elif id == "W":
            self.logger.warning(message)
        elif id == "I":
            self.logger.info(message)
        elif id == "D":
            self.logger.debug(message)
        else:
            self.logger.critical(message)
