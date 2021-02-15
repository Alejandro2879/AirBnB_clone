#!/usr/bin/python3
"""[]
"""
import uuid
import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        return("[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        if self.__dict__['created_at']:
            self.__dict__['created_at'] = self.__dict__['created_at'].isoformat()
        if "updated_at" in self.__dict__:
            self.__dict__['udated_at'] = self.__dict__['updated_at'].isoformat()
        self.__dict__['__class__'] = BaseModel.__name__
        return self.__dict__
