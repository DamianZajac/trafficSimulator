class Street:
	def __init__(self, street_name, street_number, left = "X", right = "X", up = "X", down ="X"):
		self.street_name = street_name
		self.street_number = street_number
		self.left = left
		self.right = right
		self.up = up
		self.down = down
		
	def print_header(self):
		print("Street Name\t|\tStreet Number\t|\tLeft\t|\tRight\t|\tUp\t|\tDown")
		
	def print_singular(self):
		self.print_header()
		self.print_multi()
		
	def print_multi(self):
		print("%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s" % (self.street_name, self.street_number, self.left, self.right, self.up, self.down))
		
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
		self.left = street_to_set
		street_to_set.set_right(self)
	
	def set_left(self, street_to_set):
		self.left = street_to_set
		
	def set_right_both(self, street_to_set):
		self.right = street_to_set
		street_to_set.set_left(self)
	
	def set_right(self, street_to_set):
		self.right = street_to_set
		
	def set_up_both(self, street_to_set):
		self.up = street_to_set
		street_to_set.set_down(self)
	
	def set_up(self, street_to_set):
		self.up = street_to_set
		
	def set_down_both(self, street_to_set):
		self.down = street_to_set
		street_to_set.set_up(self)
	
	def set_down(self, street_to_set):
		self.down = street_to_set