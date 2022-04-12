# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y.0   # For first release after an increment in Y
#   X.Y.Z   # For bugfix releases

__version__ = '0.1.0'

from asyncio import iscoroutinefunction
from http import HTTPStatus
from json import JSONDecodeError, loads

import jsonschema
from tornado.web import RequestHandler


def validate(schema):
    def wrapper(method):
        async def _validate(handler: RequestHandler, *args, **kwargs):
            try:
                body = loads(handler.request.body)

            except JSONDecodeError as e:
                return handler.send_error(HTTPStatus.UNPROCESSABLE_ENTITY, message=str(e))

            try:
                jsonschema.validate(instance=body, schema=schema)

            except jsonschema.exceptions.ValidationError as e:
                return handler.send_error(HTTPStatus.UNPROCESSABLE_ENTITY, message=e.message)

            if iscoroutinefunction(method):
                await method(handler, *args, body=body, **kwargs)

            else:
                method(handler, *args, body=body, **kwargs)

        return _validate

    return wrapper
