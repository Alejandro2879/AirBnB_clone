#!/usr/bin/python3
"""[Module define the BaseModel class]
"""
from datetime import datetime
import models
import uuid

_time_fmt = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    """[BaseModel class]
    """

    def __init__(self, *args, **kwargs):
        """[Define initial values to attributes]
        """
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(kwargs[key],
                                                             _time_fmt))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """[String format]
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """[Method to update 'updated_at' attribute]
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """[Return all key : values of the instance]
        """
        new = self.__dict__.copy()
        new['created_at'] = new['created_at'].isoformat()
        new['updated_at'] = new['updated_at'].isoformat()
        new['__class__'] = self.__class__.__name__
        return (new)
