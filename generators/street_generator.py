# coding=utf-8
from os.path import dirname, abspath, join
from random import choice, shuffle
from objects import street

class Street_Generator:
    def __init__(self):
        base_path = dirname(__file__)
        file_path = abspath(join(base_path, "..", "data", "street_names_list.txt"))
        with open(file_path, "r") as file:
            self.data = file.readlines()
        shuffle(self.data)
        
    def get_street(self):
        for street_name in self.data:
            yield street.Street(street_name, choice(range(100)) + 1)