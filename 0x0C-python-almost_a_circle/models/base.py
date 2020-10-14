#!/usr/bin/python3
"""
Base model class
"""
import json
import csv
import os


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if type(list_objs) != list and list_objs is not None \
                           or not all(isinstance(x, cls)for x in list_objs):
        raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                rec_fields = ['id', 'width', 'height', 'x', 'y']
                squ_fields = ['id', 'size', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rec_fields)
                else:
                    writer = csv.DictWriter(f, fieldnames=squ_fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        rec_header = ["id", "width", "height", "x", "y"]
        squ_header = ["id", "size", "x", "y"]
        header = rec_header if cls.__name__ == "Rectangle" else squ_header
        res = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for j, e in enumerate(reader):
                            if e:
                                setattr(new, header[j], str(e))
                        res.append(new)
        return res
