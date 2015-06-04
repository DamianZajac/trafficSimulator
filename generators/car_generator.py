"""
car_generator module
contains CarGenerator class
"""
from os.path import dirname, abspath, join
from random import choice, shuffle
from objects import car

class CarGenerator(object):
    """
    CarGenerator module
    generator of new cars with unique driver names and random plates
    """
    def __init__(self):
        base_path = dirname(__file__)
        file_path = abspath(join(base_path, "..", "data", "names_list.txt"))
        with open(file_path, "r") as opened_file:
            self.data = opened_file.readlines()
        self.cities = ["KR", "WA", "TK", "EL", "GD", "NO"]
        shuffle(self.data)

    def get_car(self):
        """
        get_car() -> Car
        yields another Car for every Car in data_file
        (default : names_list.txt)
        """
        for name in self.data:
            yield car.Car(driver=name, position=None, plate=self.get_plate())

    def get_plate(self):
        """
        get_plate() -> String
        returns another quasi-randomly generated plate
        drivers can be from :
        Krakow, Warsaw, Kielce, Lodz, Gdansk, Olsztyn
        """
        return "%s %s%s%s%s%s" % (choice(self.cities), choice(range(10)), \
        choice(range(10)), choice(range(10)), choice(range(10)), choice(range(10)))
