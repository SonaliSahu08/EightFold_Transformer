PROFILE_SCHEMA = {

    "type": "object",

    "properties": {

        "full_name": {
            "type": "string"
        },

        "emails": {
            "type": "array"
        },

        "phones": {
            "type": "array"
        },

        "skills": {
            "type": "array"
        }

    },

    "required": [
        "full_name"
    ]
}