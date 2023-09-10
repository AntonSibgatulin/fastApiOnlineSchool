import base64
import time


def generate_token(id: int) -> str:
    return base64.b64encode((str(time.time()) + str(id)).encode("utf-8"))
