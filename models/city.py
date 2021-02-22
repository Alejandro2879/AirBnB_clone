#!/usr/bin/python3
"""[Module define the City class]
"""

from models.base_model import BaseModel


class City(BaseModel):
    """[Create a city instance and inherits from BaseModel]
    """

    state_id = ""
    name = ""
