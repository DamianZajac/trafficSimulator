"""
street_generator module
module containt StreetGenerator class which is basically
a generator of new streets
"""
from os.path import dirname, abspath, join
from random import choice, shuffle
from objects import street

class StreetGenerator(object):
    """
    StreetGenerator class
    generator of new streets with unique street names and numbers
    """
    def __init__(self):
        base_path = dirname(__file__)
        file_path = abspath(join(base_path, "..", "data", "street_names_list.txt"))
        with open(file_path, "r") as opened_file:
            self.data = opened_file.readlines()
        shuffle(self.data)

    def get_street(self):
        """
        get_street() -> Street
        yields a new street with unique street_name and number
        """
        for street_name in self.data:
            yield street.Street(street_name, choice(range(100)) + 1)

    def data_length(self):
        """
        data_length() -> Int
        returns number of streets in the file supplied to the generator
        """
        return len(self.data)
