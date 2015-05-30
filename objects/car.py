class Car:
	def __init__(self, driver = "Ktokolwiek Ktokolwiekowy", position = "Wadowicka 1", plate = "KR 00000"):
		self.driver = driver
		self.position = position
		self.plate = plate
		self.destination = "none"
		
	def print_header(self):	
		print("Driver Name\t|\tPosition\t|\tLicence Plate")
		
	def print_singular(self):
		self.print_header()
		self.print_multi()
		
	def print_multi(self):
		print("%s\t|\t%s\t|\t%s" % (self.driver, self.position, self.plate))
		
	def set_destination(self, street):
		self.destination = street.name
		
	def get_destination(self, street):
		return self.destination