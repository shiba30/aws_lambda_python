from src.common.exec import Exec

exec = Exec()


def lambda_handler(event, context):
    exec.run(event, context)
    return
