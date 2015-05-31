import traffic_light as Tr_Light

class Street(object):
    def __init__(self, street_name, street_number, left=None, right=None, up=None, down=None):
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
        
    def get_all(self):
        return [self.up, self.right, self.down, self.left]
    
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def get_up(self):
        return self.up
        
    def get_down(self):
        return self.down
        
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
        if self.left != None:
            self.check += 1
        if self.up != None:
            self.check += 1
        if self.down != None:
            self.check += 1
        if self.right != None:
            self.check += 1
        if self.check > 2:
            self.traffic_lights = Tr_Light.Traffic_Light(street_parent = self)
            
    def get_lights(self):
        if self.traffic_lights == None:
            print(self, "This is not a crossroad, hence no lights to return!")
        return self.traffic_lights
        
    def is_crossroad(self):
        if self.traffic_lights == None:
            return False
        else:
            return True