#!/usr/bin/python3
"""[Module define the review class]
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """[Create new review instance and inherits from BaseModel]
    """

    place_id = ""
    user_id = ""
    text = ""
