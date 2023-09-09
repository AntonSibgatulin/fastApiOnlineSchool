from fastapi import Request


def get_token(request: Request):
    return request.query_params.get("token")
