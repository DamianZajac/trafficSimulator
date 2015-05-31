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
        print("Street Parent\t|\tHorizontal\t|\tVertical")
        return self
        
    def print_singular(self):
        self.print_header()
        self.print_multi()
        return self
        
    def print_multi(self):
        print("%s\t|\t%s %s\t|\t%s %s" % (self.street_parent, self.horizontal_light, self.switch_delay_horizontal, self.vertical_light, self.switch_delay_vertical))
        return self
        
    def switch_lights(self, timer):
        help_timer = timer
        while help_timer > 0:
            help_timer -= self.switch_delay_horizontal
            help_timer -= self.switch_delay_vertical
        if help_timer == 0:
            print "Successfully switched lights (horizontal ON)"
            self.horizontal_light = Traffic_Light.GREEN 
            self.vertical_light = Traffic_Light.RED
        else:
            if help_timer + self.switch_delay_vertical == 0:
                print "Successfully switched lights (vertical ON)"
                self.horizontal_light = Traffic_Light.RED
                self.vertical_light = Traffic_Light.GREEN
        return self
        
    def get_horizontal_status(self):
        return self.horizontal_light
    
    def get_vertical_status(self):
        return self.vertical_light
        
    def get_delay_horizontal(self):
        return self.switch_delay_horizontal
    
    def get_delay_vertical(self):
        return self.switch_delay_vertical
        
    def set_delay_horizontal(self, switch_delay):
        self.switch_delay_horizontal = switch_delay
        return self
        
    def set_delay_vertical(self, switch_delay):
        self.switch_delay_vertical = switch_delay
        return self
        
    def set_delays(self, horizontal, vertical):
        self.set_delay_horizontal(horizontal)
        self.set_delay_vertical(vertical)
        return self