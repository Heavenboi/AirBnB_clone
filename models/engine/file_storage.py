#!/usr/bin/python3

from datetime import datetime
import json
import models

class FileStorage:
    ''' Private class attribute '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary."""
        key = str(type(obj).__name__) + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized = {key: obj.to_dict() for key,
                      obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                content = file.read()
                if content is None:
                    return
                objects_dict = json.loads(content)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_key = f"{class_name}.{obj_id}"
                if obj_key not in FileStorage.__objects:
                    class_definition = globals().get(class_name)
                    if class_definition:
                        obj = class_definition(**value)
                        FileStorage.__objects[obj_key] = obj
        except FileNotFoundError:
            pass
