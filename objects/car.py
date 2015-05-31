from random import choice

class Car:
    def __init__(self, driver, position, plate = "KR 00000"):
        self.driver = driver
        self.position = position
        self.plate = plate
        self.destination = None
        self.came_from = None
        self.position_to_move = None
        
    def print_header(self):    
        print "Driver Name\t|\tPosition\t|\tLicence Plate"
        return self
        
    def print_singular(self):
        self.print_header()
        self.print_multi()
        return self
        
    def print_multi(self):
        print "%s\t|\t%s\t|\t%s" % (self.driver, self.position, self.plate)
        return self
        
    def set_position(self, street):
        self.position = street
        return self
        
    def get_position(self):
        return self.position

    def set_destination(self, street):
        self.destination = street.name
        return self
        
    def get_destination(self, street):
        return self.destination
        
    def is_at_destination(self):
        if self.position == self.destination:
            return True
        return False
        
    def get_moves(self):
        helper_position = self.position
        return [helper_position.get_left(), helper_position.get_right(), helper_position.get_up(), helper_position.get_down()]
        
    def move(self):
        possible_moves = self.get_moves()
        if self.position_to_move == None or self.position_to_move not in possible_moves:
            possible_moves = filter(lambda x: x is not None and x != self.came_from, possible_moves)
            if possible_moves == []:
                self.position_to_move = self.came_from
            else:
                self.position_to_move = choice(possible_moves)
        (came_from_where, check) = self.is_possible()
        if check:
            self.position = self.position_to_move
            self.came_from = came_from_where
        return self
    def is_possible(self):
        direction = None
        return_bool = False
        if self.position.up == self.position_to_move:
            if self.position.is_crossroad() == False or self.position.get_lights().get_vertical_status():
                direction = "down"
            else:
                print "Vertical lights are red, waiting for light change"
        elif self.position.right == self.position_to_move:
            if self.position.is_crossroad() == False or self.position.get_lights().get_horizontal_status():
                direction = "left"
            else:
                print "Horizontal lights are red, waiting for light change"
        elif self.position.down == self.position_to_move:
            if self.position.is_crossroad() == False or self.position.get_lights().get_vertical_status():
                direction = "up"
            else:
                print "Vertical lights are red, waiting for light change"
        elif self.position.left == self.position_to_move:
            if self.position.is_crossroad() == False or self.position.get_lights().get_horizontal_status():
                direction = "right"
            else:
                print "Horizontal lights are red, waiting for light change"
        if direction != None:
            return_bool = True
            direction = self.position
        return (direction, return_bool)