import os

from dotenv import load_dotenv

from common.exec import Exec

load_dotenv()
run_dev = os.getenv("RUN_DEV")

exec = Exec()

if run_dev == "lambda":

    def lambda_handler(event, context):
        exec.run(event, context)
        return

else:
    if __name__ == "__main__":
        exec.run()
