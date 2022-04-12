from asyncio import iscoroutinefunction
from http import HTTPStatus
from json import JSONDecodeError, loads

import jsonschema
from pkg_resources import get_distribution
from tornado.web import RequestHandler

__version__ = get_distribution('tornado-jsonschema').version


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
