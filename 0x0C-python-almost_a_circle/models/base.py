#!/usr/bin/python3
"""
Base model class
"""
import json
import csv

class Base:
    """
    Class module for Base model
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """"initialises class Base and sets instance id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)


    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        di = []
        if list_objs is not None:
            for i in list_objs:
                di.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(di))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            test = cls(1, 1)
        elif cls.__name__ is "Square":
            test = cls(1)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls. frrom_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l
