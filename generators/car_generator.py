from os.path import dirname, abspath, join
from random import choice, shuffle
from objects import car
import re

class Car_Generator:
	def __init__(self):
		base_path = dirname(__file__)
		file_path = abspath(join(base_path, "..", "data", "names_list.txt"))
		with open(file_path, "r") as file:
			self.data = file.readlines()
		self.cities = ["KR", "WA", "TK", "EL", "GD", "OL"]
		shuffle(self.data)
		
	def get_car(self, current_street_list):
		for name in self.data:
			yield car.Car(driver = name, position = choice(current_street_list), plate = self.get_plate())
			
	def get_plate(self):
		return "%s %s%s%s%s%s" % (choice(self.cities), choice(range(10)), choice(range(10)), choice(range(10)), choice(range(10)), choice(range(10)))