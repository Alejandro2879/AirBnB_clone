#!/usr/bin/python3
"""[]
"""
import json
from models.base_model import BaseModel
import models


class FileStorage:
    """[]
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """[]
        """
        if cls is not None:
            new = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new[key] = value
            return (new)
        return self.__objects

    def new(self, obj):
        """[]
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        j_obj = {}
        for key in self.__objects:
            j_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as doc:
            json.dump(j_obj, doc)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as doc:
                j_obj  = json.load(doc)
            for key in j_obj:
                self.__objects[key] = j_obj[key]["__class__"](**j_obj[key])
        except:
            pass

