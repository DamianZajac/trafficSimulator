class Traffic_Light:
	GREEN = True
	RED = False
	
	def __init__(self, street_parent, switch_delay = 15):
		self.street_parent = street_parent
		self.horizontal_light = Traffic_Light.GREEN
		self.vertical_light = Traffic_Light.RED
		self.switch_delay = switch_delay
		
	def print_header(self):
		print("Street Parent\t|\tHorizontal Status\t|\tVertical Status")
		return self
		
	def print_singular(self):
		self.print_header()
		self.print_multi()
		return self
		
	def print_multi(self):
		print("%s\t|\t%s\t|\t%s" % (self.street_parent, self.horizontal_light, self.vertical_light))
		return self
		
	def switch_lights(self):
		self.horizontal_light = not self.horizontal_light
		self.vertical_light = not self.vertical_light
		return self
		
	def get_delay(self):
		return self.switch_delay
		
	def set_delay(self, switch_delay):
		self.switch_delay = switch_delay
		return self