from os import getenv
from typing import Optional

from .types import GetHandlerType, PostHandlerType
from .parsers import parse_query, parse_headers, parse_body
from .handler import handle
from .composers import compose_response
from .exceptions import ApiException


def run(
    get: Optional[GetHandlerType] = None,
    post: Optional[PostHandlerType] = None,
    verbose: bool = True,
):
    method = getenv("REQUEST_METHOD", "")
    query = parse_query()
    headers = parse_headers()
    body = parse_body(headers)
    try:
        response = handle(method, query, headers, body, get=get, post=post)
    except ApiException as e:
        response = e.compose()
    result = compose_response(*response)
    if verbose:
        print(result)
    return result
