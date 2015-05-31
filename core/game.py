"""
Game class - all control of real time events is being done in this class
it decides on objects creation, time control, GFX, everything
"""
from generators import street_generator as str_gen, car_generator as car_gen
from random import choice
from time import sleep
import msvcrt, types

class Game(object):
    def __init__(self, os_type="WIN32", street_number=1, car_number=0):
        self.street_gen = str_gen.Street_Generator()
        self.car_gen = car_gen.Car_Generator()
        self.os_type = os_type
        self.street_list = []
        self.car_list = []
        self.create_streets(street_number)
        self.create_cars(car_number)
        self.timer = 0

    def run(self):
        if self.os_type == "WIN32":
            loop_bool = True
            print "Starting the whole thing with", len(self.street_list), " streets and", len(self.car_list), " cars"
            while loop_bool:
                print "Current turn (press <ESC> to stop the testing) :", self.timer
                self.move_cars()
                self.check_and_switch_lights()
                self.timer += 1
                sleep(1)
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 27:
                        print "<ESC> press detected stopping the testing loop"
                        loop_bool = False
                if self.car_list == []:
                    print "200 cars reached their destination, stopping the simulation"
                    loop_bool = False
        else:
            pass
            
    def move_cars(self):
        for index, car in enumerate(self.car_list):
            if isinstance(car, types.GeneratorType):
                break
            car.move()
            if car.did_car_move():
                print car, " moved to ", car.get_position()
            if car.is_at_destination():
                print car, " reached his destination, removing him from the car list and adding a new driver"
                del self.car_list[index]
                self.create_cars(1)

    def check_and_switch_lights(self):
        for street in self.street_list:
            if street.is_crossroad():
                street.get_lights().switch_lights(self.timer)

    def create_streets(self, street_number):
        for _ in range(street_number):
            new_street = self.street_gen.get_street()
            self.street_list.append(new_street)
            self.show_street(new_street)
            
    def create_cars(self, car_number):
        for _ in range(car_number):
            new_car = self.car_gen.get_car(choice(self.street_list))
            self.car_list.append(new_car)
            self.show_car(new_car)
            
    def show_car(self, car):
        """
        in the future it will show the car on the map
        """
        pass
        
    def show_street(self, street):
        """
        in the future it will show the street on the map
        """
        pass
        
    def set_street_list(self, street_list):
        self.street_list = street_list

    def set_car_list(self, car_list):
        self.car_list = car_list