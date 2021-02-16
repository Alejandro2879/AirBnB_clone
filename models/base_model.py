#!/usr/bin/python3
"""[Module define the BaseModel class]
"""
import uuid
from datetime import datetime


class BaseModel:
    """[BaseModel class]
    """

    def __init__(self, *args, **kwargs):
        """[Define initial values to attributes]
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)



        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """[String format]
        """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """[Method to update 'updated_at' attribute]
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """[Return all key : values of the instance]
        """
        new = self.__dict__.copy()
        if 'created_at' in new:
            new['created_at'] = new['created_at'].isoformat()
        if 'updated_at' in new:
            new['udated_at'] = new['updated_at'].isoformat()
        new['__class__'] = self.__class__.__name__
        return new
