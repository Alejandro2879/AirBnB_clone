#!/usr/bin/python3
"""[Module define the BaseModel class]
"""
from datetime import datetime
import models
import uuid

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
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = kwargs[created_at].isoformat()
            else:
                self.created_at = datetime.now()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = kwargs[updated_at].isoformat()
            else:
                self.updated_at = kwargs[updated_at].isoformat()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """[String format]
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """[Method to update 'updated_at' attribute]
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        

    def to_dict(self):
        """[Return all key : values of the instance]
        """
        new = self.__dict__.copy()
        if 'created_at' in new:
            new['created_at'] = new['created_at'].isoformat()
        if 'updated_at' in new:
            new['updated_at'] = new['updated_at'].isoformat()
        new['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in new:
            del new['_sa_instance_state']
        return new
