add_tabs_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string", "minLength": 1},
        "data_points": {"type": "array",
                        "properties": {
                            "data_type": {"type": "string", "minLength": 1},
                            "label": {"type": "string", "minLength": 1},
                            "placeholder": {"type": "string", "minLength": 1},
                            "description": {"type": "string", "minLength": 1},
                            "options": {"type": "string", "enum": ["0", "1", "2", "3", "4", "5" "unknown"],
                                        "default": "unknown", "minLength": 1},

                        },
                        "required": ["data_type", "label", "description"],
                        "anyOf": [
                            {"required": ["options"]},
                            {"required": ["placeholder"]}]
                        }
    },
    "required": ["name", "description", "data_points"]
}


