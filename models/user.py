#!/usr/bin/python3
"""the first User class, which inherits from BaseModel"""


class User(BaseModel):
    """a class User which inherits from BaseModel
    Attributes:
        email (string)
        password (string)
        first_name (string)
        last_name (string)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
