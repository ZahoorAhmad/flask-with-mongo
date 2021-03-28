from logging import getLogger
from functools import wraps
from flask import Response, request
from jsonschema import validate, ValidationError, FormatChecker

LOGGER = getLogger("json_validator.py")


def validate_json(schema=None):
    """Validate input data regardless of the content type whether its a valid json or not"""

    def json_decorator(func):
        @wraps(func)
        def json_validator(*args, **kwargs):
            data = request.get_json(force=True)
            if not data:
                return Response(status=400)
            if schema:
                try:
                    validate(data, schema, format_checker=FormatChecker())
                except ValidationError as e:
                    LOGGER.info(e.message)
                    return Response(status=400)

            return func(*args, **kwargs)

        return json_validator

    return json_decorator
