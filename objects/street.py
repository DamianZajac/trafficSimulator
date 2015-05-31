import traffic_light as Tr_Light

class Street:
	def __init__(self, street_name, street_number, left = "X", right = "X", up = "X", down ="X"):
		self.street_name = street_name
		self.street_number = street_number
		self.left = left
		self.right = right
		self.up = up
		self.down = down
		self.traffic_lights = None
		
	def print_header(self):
		print("Street Name\t|\tStreet Number\t|\tLeft\t|\tRight\t|\tUp\t|\tDown")
		return self
		
	def print_singular(self):
		self.print_header()
		self.print_multi()
		return self
		
	def print_multi(self):
		print("%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s" % (self.street_name, self.street_number, self.left, self.right, self.up, self.down))
		return self
		
	def __repr__(self):
		return ("%s %s" % (self.street_name, self.street_number))
		
	def find_left(self):
		if self.left != "X":
			return self.left
		return None
		
	def find_right(self):
		if self.right != "X":
			return self.right
		return None
		
	def find_up(self):
		if self.up != "X":
			return self.up
		return None
		
	def find_down(self):
		if self.down != "X":
			return self.down
		return None
		
	def set_left_both(self, street_to_set):
		street_to_set.set_right(self)
		self.set_left(street_to_set)
		return self
		
	def set_left(self, street_to_set):
		self.left = street_to_set
		self.check_and_set_lights()
		
	def set_right_both(self, street_to_set):
		street_to_set.set_left(self)
		self.set_right(street_to_set)
		return self
		
	def set_right(self, street_to_set):
		self.right = street_to_set
		self.check_and_set_lights()
		
	def set_up_both(self, street_to_set):
		street_to_set.set_down(self)
		self.set_up(street_to_set)
		return self
		
	def set_up(self, street_to_set):
		self.up = street_to_set
		self.check_and_set_lights()
		
	def set_down_both(self, street_to_set):
		street_to_set.set_up(self)
		self.set_down(street_to_set)
		return self
		
	def set_down(self, street_to_set):
		self.down = street_to_set
		self.check_and_set_lights()
		
	def check_and_set_lights(self):
		self.check = 0
		if self.left != "X":
			self.check += 1
		if self.up != "X":
			self.check += 1
		if self.down != "X":
			self.check += 1
		if self.right != "X":
			self.check += 1
		if self.check > 2:
			self.traffic_lights = Tr_Light.Traffic_Light(street_parent = self)
			
	def get_lights(self):
		if self.traffic_lights == None:
			print("This is not a crossroad, hence no lights to return!")
		return self.traffic_lights
		
	def is_crossroad(self):
		if self.traffic_lights == None:
			return False
		else:
			return True