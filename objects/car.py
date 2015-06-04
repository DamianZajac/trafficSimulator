from random import choice

class Car(object):
    def __init__(self, driver, position, plate="KR 00000"):
        self.driver = driver
        self.position = position
        self.plate = plate
        self.move_count = 0
        self.destination = None
        self.came_from = None
        self.position_to_move = None
        
    def __repr__(self):
        return self.driver
        
    def print_header(self):    
        print "Driver Name\t|\tPosition\t|\tDestination\t|\tLicence Plate"
        return self
        
    def print_singular(self):
        self.print_header()
        self.print_multi()
        return self
        
    def print_multi(self):
        print "%s\t|\t%s\t|\t%s\t|\t%s" % (self.driver, self.position, self.destination, self.plate)
        return self
        
    def get_move_count(self):
        return self.move_count
    
    def set_position(self, street):
        self.position = street
        return self
        
    def get_position(self):
        return self.position

    def set_destination(self, street):
        self.destination = street
        return self
        
    def get_destination(self, street):
        return self.destination
        
    def is_at_destination(self):
        if self.position == self.destination:
            return True
        return False
        
    def did_car_move(self):
        if self.position_to_move == None:
            return True
        return False
        
    def get_moves(self):
        return self.position.get_all()
        
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
            self.position_to_move = None
            self.move_count += 1
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