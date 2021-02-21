#!/usr/bin/python3
"""[Module define the FileStorage class]
"""
import json
from models.base_model import BaseModel
import models

__valid_models = {'BaseModel': BaseModel}


class FileStorage:
    """[serializes instances to a JSON file
        and deserializes JSON file to instances]
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """[Returns the dictionary __objects]
        """
        return (self.__objects)

    def new(self, obj):
        """[Sets in __objects the obj with key <obj class name>.id]
        """
        self.__objects[str(obj.__class__.__name__) + '.' + str(obj.id)] = obj

    def save(self):
        """[Serializes __objects to the JSON file (path: __file_path)]
        """
        j_obj = {}
        for key in self.__objects:
            j_obj[key] = self.__objects[key].to_dict()

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
