#!/usr/bin/python3
"""[]
"""
import json


class FileStorage:
    """[]
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """[]
        """
        if cls is not None:
            new = {}
            for key, value in self.__objects.items():
                if value.__class__.__name__ == cls:
                    new[key] = value
            return (new)
        else:
            return (self.__objects)

    def new(self, obj):
        """[]
        """
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        to_json = {}
        for key in self.__objects:
            to_json[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, 'w') as doc:
            json.dump(to_json, doc)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as doc:
                j_obj  = json.load(doc)
                for key in j_obj:
                    self.__objects[key] = j_obj[key]
        except:
            pass

