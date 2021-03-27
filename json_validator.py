from flask import Response
from jsonschema import validate, ValidationError
from schema import add_tabs_schema

record = {"name": "ad", "description": "erer", "data_points":
    [
        {"data_type": "234", "label": 45, "description": "testings", "placeholder": "gb/3"}
    ]
          }


def validate_json(schem, payload):
    try:
        print(validate(instance=payload, schema=schem))
    except ValidationError:
        return Response(status=400)