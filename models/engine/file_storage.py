#!/usr/bin/python3
"""A storage moudle.
"""
import json


class FileStorage:
    """A class that serializes instances to a JSON file and deserilaizes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary objects
        """
        from models.base_model import BaseModel
        obj_dict = {}
        for key in __class__.__objects.keys():
            obj = __class__.__objects[key]
            obj_dict[key] = BaseModel(**obj)
        return obj_dict

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        key = obj["__class__"] + "." + obj["id"]
        __class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        with open(__class__.__file_path, "w") as wr:
            json.dump(__class__.__objects, wr)

    def reload(self):
        """Deserializes the JSON file to __objects. only if the
        JSON file (__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception raised
        """
        try:
            with open(__class__.__file_path) as rd:
                __class__.__objects = json.load(rd)
        except FileNotFoundError:
            pass
