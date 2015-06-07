"""
car module
contains Car class implementation
"""
# -*- coding: utf-8 -*-
from random import choice
from copy import copy
from itertools import chain
from time import sleep

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
        self.counters = [0, 0]
        self.destination = None
        self.came_from = None
        self.position_to_move = None       
        self.directions_to_move = []
        self.found = False

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
        makes the car move in a random direction
        doesn't change mind of direction taken
        """
        self.counters[1] += 1
        possible_moves = self.get_moves()
        before_pos = self.position_to_move
        if self.position_to_move == None or self.position_to_move not in possible_moves:
            possible_moves = [street for street in possible_moves \
                if street is not None and street != self.came_from]
            if possible_moves == []:
                self.position_to_move = self.came_from
            else:
                self.position_to_move = choice(possible_moves)
        (came_from_where, check) = self.is_possible()
        if check:
            self.position.remove_car(self)
            self.position = self.position_to_move
            self.position.add_car(self)
            self.came_from = came_from_where
            self.position_to_move = None
            self.counters[0] += 1
        return self

    def zombie_move(self):
        """makes the car move in a "zombie" way as in super random every turn
        can (and propably will) backtrack in its own steps a lot
        """
        self.position_to_move = choice([s for s in self.get_moves() if s is not None])
        return self.move()

    def fastest_move(self):
        """makes the car move in a shortest way possible
        """
        if self.directions_to_move == []:
            lst = self.find_destination_path(self.position, [], {})
            lst = self.remove_brackets(lst)
            self.directions_to_move = lst
            if type(self.directions_to_move) is list:
                del self.directions_to_move[0]
        if self.position_to_move == None and self.position != self.destination and self.directions_to_move != None:
            self.position_to_move = self.directions_to_move[0]
            del self.directions_to_move[0]
        return self.move()

    def remove_brackets(self, lst):
        """simple function that just gets the proper list from lists of lists of .... lists
        for example from
        [[[[[["co"]]]]]]
        it gets
        ["co"]
        """
        if type(lst) != list:
            return lst
        bool_check = True
        while bool_check:
            if type(lst[0]) != list:
                return lst
            else:
                lst = lst[0]
        
    def find_destination_path(self, street, lst, visited_dict):
        """simple BFS-sort of algorithm for finding shortest path to destination
        """
        new_lst = copy(lst)
        if street == None or street in visited_dict or self.found:
            return None
        visited_dict[street] = True
        new_lst.append(street)
        if self.destination == street:
            self.found = True
            return new_lst
        go_left = self.find_destination_path(street.left, new_lst, visited_dict)
        go_right = self.find_destination_path(street.right, new_lst, visited_dict)
        go_up = self.find_destination_path(street.up, new_lst, visited_dict)
        go_down = self.find_destination_path(street.down, new_lst, visited_dict)
        direction_array = [dir for dir in [go_left, go_right, go_up, go_down] if dir is not None]
        if direction_array != []:
            return direction_array
        
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
