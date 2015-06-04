"""
car module
contains Car class implementation
"""
from random import choice

class Car(object):
    """
    Car class
    class that implements a Car object
    it has a driver name and plates
    it has a position (Street) and a final destination (Street)
    """
    def __init__(self, driver, position, plate):
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
        """
        print_header() -> void
        prints header for print table
        """
        print "Driver Name\t|\tPosition\t|\tDestination\t|\tLicence Plate"
        return self

    def print_multi(self):
        """
        print_multi() -> void
        prints data about the car
        """
        print "%s\t|\t%s\t|\t%s\t|\t%s" % (self.driver, self.position, self.destination, self.plate)
        return self

    def set_position(self, street):
        """
        set_position(Street street) -> self
        sets position to given "street"
        return itself
        """
        self.position = street
        return self

    def set_destination(self, street):
        """
        set_destination(Street street) -> self
        sets destination to given "street"
        returns itself
        """
        self.destination = street
        return self

        return self.destination

    def is_at_destination(self):
        """
        is_at_destination() -> Bool
        returns True if its position is equal to its destination
        returns False otherwise
        """
        return self.position == self.destination

    def did_car_move(self):
        """
        did_car_move() -> Bool
        returns True if the car has moved in the last turn
        returns False otherwise
        """
        return self.position_to_move == None

    def get_moves(self):
        """
        get_moves() -> Street -> Street *
        returns all possible streets the car can go to in 1 turn from its current position
        """
        return self.position.get_all()

    def move(self):
        """
        move() -> self
        makes the car move
        """
        possible_moves = self.get_moves()
        if self.position_to_move == None or self.position_to_move not in possible_moves:
            possible_moves = [street for street in possible_moves \
                if street is not None and street != self.came_from]
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
        """
        is_possible() -> (Street, Boolean)
        returns a tuple of (street_that_can_be_gone_to, True) if it can go there
        return a tuple of (None, False) if it can't go to the chosen street
        """
        direction = None
        return_bool = False
        if self.position.up == self.position_to_move:
            if self.position.is_crossroad() == False or \
            self.position.traffic_lights.vertical_light:
                direction = "down"
                return_bool = True
                direction = self.position
            else:
                print "Vertical lights are red, waiting for light change"
        elif self.position.right == self.position_to_move:
            if self.position.is_crossroad() == False or \
            self.position.traffic_lights.horizontal_light:
                direction = "left"
                return_bool = True
                direction = self.position
            else:
                print "Horizontal lights are red, waiting for light change"
        elif self.position.down == self.position_to_move:
            if self.position.is_crossroad() == False or \
            self.position.traffic_lights.vertical_light:
                direction = "up"
                return_bool = True
                direction = self.position
            else:
                print "Vertical lights are red, waiting for light change"
        elif self.position.left == self.position_to_move:
            if self.position.is_crossroad() == False or \
            self.position.traffic_lights.horizontal_light:
                direction = "right"
                return_bool = True
                direction = self.position
            else:
                print "Horizontal lights are red, waiting for light change"
        return (direction, return_bool)
