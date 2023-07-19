from configs.db import dbConnection

userCollection = dbConnection['users']

user_schema = {'name': str, 'age': int, 'email': str, 'password': str,
               'membership': str, 'bio': str, 'date_of_birth': str}


def validate_data(data, schema):
    for key, value_type in schema.items():
        if key not in data or not isinstance(data[key], value_type):
            return False
    return True
