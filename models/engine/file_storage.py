#!/usr/bin/python3
"""[Module define the FileStorage class]
"""
import json
from models.base_model import BaseModel
import models
import os.path



class FileStorage:
    """[serializes instances to a JSON file
        and deserializes JSON file to instances]
    """
    __file_path = 'file.json'
    __objects = {}

    """List of valid models"""
    __valid_models = {'BaseModel': BaseModel}

    def valid_models(self):
        """[return dictionary __objects]
        """
        return (type(self).__valid_models)

    def all(self, cls=None):
        """[Returns the dictionary __objects]
        """
        return (type(self).__objects)

    def new(self, obj):
        """[Sets in __objects the obj with key <obj class name>.id]
        """
        if obj:
            type(self).__objects[str(obj.__class__.__name__) + '.' + obj.id] = obj

    def save(self):
        """[Serializes __objects to the JSON file (path: __file_path)]
        """
        j_obj = type(self).__objects.copy()

        for key in j_obj:
            j_obj[key] = j_obj[key].to_dict()

        with open(self.__file_path, 'w') as n_file:
            json.dump(j_obj, n_file)

    def reload(self):
        """[Deserializes the JSON file to __objects]
        """
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path) as n_file:
                json_f = json.load(n_file)

            for key in json_f:
                new = json_f[key]['__class__']
                type(self).__objects[key] = type(self).__valid_models[new](
                    **json_f[key])
