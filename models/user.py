#!/usr/bin/python3
"""[Module define de User class]
"""

from models.base_model import BaseModel


class User(BaseModel):
    """[Create an user instance and inherits from BaseModel]
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
