class Traffic_Light:
	GREEN = True
	RED = False
	
	def __init__(self, street_parent, switch_delay_horizontal = 15, switch_delay_vertical = 15):
		self.street_parent = street_parent
		self.horizontal_light = Traffic_Light.GREEN
		self.vertical_light = Traffic_Light.RED
		self.switch_delay_horizontal = switch_delay_horizontal
		self.switch_delay_vertical = switch_delay_vertical
		
	def print_header(self):
		print("Street Parent\t|\tHorizontal Status and delay\t|\tVertical Status and delay")
		return self
		
	def print_singular(self):
		self.print_header()
		self.print_multi()
		return self
		
	def print_multi(self):
		print("%s\t|\t%s %s\t|\t%s %s" % (self.street_parent, self.horizontal_light, self.switch_delay_horizontal, self.vertical_light, self.switch_delay_vertical))
		return self
		
	def switch_lights(self):
		self.horizontal_light = not self.horizontal_light
		self.vertical_light = not self.vertical_light
		return self
		
	def get_delay_horizontal(self):
		return self.switch_delay_horizontal
	
	def get_delay_horizontal(self):
		return self.switch_delay_vertical
		
	def set_delay_vertical(self, switch_delay):
		self.switch_delay_vertical = switch_delay
		return self
		
	def set_delay_vertical(self, switch_delay):
		self.switch_delay_vertical = switch_delay
		return self