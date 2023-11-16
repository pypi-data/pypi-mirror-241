"""JSON RPC request and response parsing."""
__all__ = ("parse_request",)

import json
import logging
import traceback
from json import JSONDecodeError
from typing import Any, Optional, Union

from pydantic import ValidationError

from jsonrpcobjects.errors import INVALID_REQUEST, PARSE_ERROR
from jsonrpcobjects.objects import (
    BatchType,
    DataError,
    Error,
    ErrorResponse,
    Notification,
    NotificationType,
    ParamsNotification,
    ParamsRequest,
    Request,
    RequestType,
)

log = logging.getLogger("jsonrpc")


def parse_request(
    data: Union[bytes, str], debug: bool = False
) -> Union[ErrorResponse, NotificationType, RequestType, BatchType]:
    """Parse a JSON RPC request."""
    parsed_json = _get_parsed_json(data, debug)
    if isinstance(parsed_json, list):
        return [_parse_request(it, debug) for it in parsed_json]
    elif isinstance(parsed_json, ErrorResponse):
        return parsed_json
    return _parse_request(parsed_json, debug)


def _parse_request(
    parsed_json: Any, debug: bool
) -> Union[ErrorResponse, NotificationType, RequestType]:
    try:
        is_request = parsed_json.get("id") is not None
        has_params = parsed_json.get("params") is not None
        if is_request:
            return (
                ParamsRequest(**parsed_json) if has_params else Request(**parsed_json)
            )
        return (
            ParamsNotification(**parsed_json)
            if has_params
            else Notification(**parsed_json)
        )
    # Invalid JSON-RPC 2.0 request.
    except (TypeError, ValidationError) as error:
        return _get_error(parsed_json.get("id"), error, INVALID_REQUEST, debug)
    # JSON was not JSON object.
    except AttributeError as error:
        return _get_error(None, error, INVALID_REQUEST, debug)


def _get_parsed_json(
    data: Union[bytes, str], debug: bool
) -> Union[ErrorResponse, dict, list]:
    try:
        parsed_json = json.loads(data)
    except (TypeError, JSONDecodeError) as error:
        return _get_error(None, error, PARSE_ERROR, debug)
    return parsed_json


def _get_error(
    id: Optional[Union[int, str]], error: Exception, base_error_type: Error, debug: bool
) -> ErrorResponse:
    log.exception("%s:", type(error).__name__)
    if debug:
        tb = traceback.format_list(traceback.extract_tb(error.__traceback__))
        rpc_error = DataError(
            code=base_error_type.code,
            message=base_error_type.message,
            data=f"{type(error).__name__}\n{tb}",
        )
    else:
        rpc_error = Error(code=base_error_type.code, message=base_error_type.message)
    return ErrorResponse(id=id, error=rpc_error)
