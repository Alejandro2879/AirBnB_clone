#!/usr/bin/python3
"""[Module define the FileStorage class]
"""
import json
from models.base_model import BaseModel
import models


class FileStorage:
    """[serializes instances to a JSON file
        and deserializes JSON file to instances]
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """[Returns the dictionary __objects]
        """
        if cls is not None:
            new = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new[key] = value
            return (new)
        return self.__objects

    def new(self, obj):
        """[Sets in __objects the obj with key <obj class name>.id]
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """[Serializes __objects to the JSON file (path: __file_path)]
        """
        j_obj = {}
        for key in self.__objects:
            j_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as doc:
            json.dump(j_obj, doc)

    def reload(self):
        """[Deserializes the JSON file to __objects]
        """
        try:
            with open(self.__file_path, 'r') as doc:
                j_obj = json.load(doc)
            for key in j_obj:
                self.__objects[key] = j_obj[key]["__class__"](**j_obj[key])
        except:
            pass
