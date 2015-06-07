"""
Game class - all control of real time events is being done in this class
it decides on objects creation, time control, GFX, everything
"""
from generators import street_generator as str_gen, car_generator as car_gen
from core import settings as settings
from random import choice
from time import sleep
import msvcrt

class Game(object):
    """
    Game - class controlling whole app
    real time events, objects creation, GFX
    """
    def __init__(self, settings_init=settings.Settings(), street_number=0, car_number=0):
        self.street_gen = str_gen.StreetGenerator().get_street()
        self.car_gen = car_gen.CarGenerator().get_car()
        self.street_list = []
        self.car_list = []
        self.create_streets(street_number)
        self.create_cars(car_number)
        self.timer = 1
        self.car_stats = []
        self.settings = settings_init

    def run(self):
        """
        run() -> void
        runs the live-application
        """
        if self.settings['os'] == "WIN32":
            loop_bool = True
            print "Starting the whole thing with %s streets and %s cars" % \
            (len(self.street_list), len(self.car_list))
            while loop_bool:
                print "Current turn (press <ESC> to stop the testing) :", self.timer
                self.move_cars()
                self.check_and_switch_lights()
                self.print_cars()
                self.timer += self.settings['timer']
                sleep(0.0001)
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 27:
                        print "<ESC> press detected stopping the testing loop"
                        loop_bool = False
                if self.car_list == [] or \
                  self.settings['car_counter'] >= self.settings['car_limit']:
                    print "200 cars reached their destination, stopping the simulation"
                    loop_bool = False
        else:
            pass
        self.show_stats()

    def move_cars(self):
        """
        move_cars() -> void
        moves all cars with currently used way of moving
        """
        for index, car in enumerate(self.car_list):
            if self.settings['move_type'] == 'normal':
                car.fastest_move()
            elif self.settings['move_type'] == 'zombie':
                car.zombie_move()
            else:
                car.move()
            if car.did_car_move():
                print car, " moved to ", car.position
            if car.is_at_destination():
                print car, " reached his destination, removing him from the \
                    car list and adding a new driver"
                self.remove_and_add_car(index, car)
                del self.car_list[index]
                self.create_cars(1)

    def remove_and_add_car(self, index, car):
        """removes and adds a car to the car list
        also calls function to add stats about car movements
        """
        del self.car_list[index]
        self.create_cars(1)
        self.get_stats(car)
        car.position.remove_car(car)
        self.settings['car_counter'] += 1

    def get_stats(self, car):
        """gets stats from car object to local list
        """
        self.car_stats.append(car.counters)

    def check_and_switch_lights(self):
        """
        check_and_switch_lights() -> void
        checks every street whether its a crossroad and then
        checks and switches lights on them accordingly to settings
        """
        for street in self.street_list:
            if street.is_crossroad():
                street.traffic_lights.switch_lights(self.timer)

    def create_streets(self, street_number):
        """
        create_streets(int N) -> Street
        creates "N" new streets, does not try to randomly connect them
        will return the street if "N" is equal to 1
        """
        for _ in range(street_number):
            try:
                new_street = next(self.street_gen)
                self.street_list.append(new_street)
                if street_number == 1:
                    return new_street
            except StopIteration:
                self.street_gen = str_gen.StreetGenerator().get_street()
                self.create_streets(1)

    def create_cars(self, car_number):
        """
        create_cars(int N) -> Car
        creates "N" new cars, gives them random starting position and destination
        selected from current street list
        will return the car if "N" is equal to 1
        """
        for _ in range(car_number):
            try:
                new_car = next(self.car_gen)
                new_car.position = choice(self.street_list)
                new_car.position.add_car(new_car)
                new_car.destination = choice(self.street_list)
                self.car_list.append(new_car)
                self.settings['car_counter'] += 1
                if car_number == 1:
                    return new_car
            except StopIteration:
                self.car_gen = car_gen.CarGenerator().get_car()
                self.create_cars(1)

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

    def show_stats(self):
        """shows car movement stats
        """
        sum_moves, sum_turns = 0.0, 0.0
        for moves, turns in self.car_stats:
            sum_moves += moves
            sum_turns += turns
        print "Total moves for cars: %d\t|\tTotal turns for cars: %d\t|\tTurns elapsed : %d" \
            % (sum_moves, sum_turns, self.timer)
        print "Percentage of moving : %.2f%%\t|\tPercentage of waiting : %.2f%%" % \
          ((sum_moves / sum_turns * 100), ((sum_turns - sum_moves) / sum_turns * 100))

    def print_cars(self):
        """
        print_cars() -> void
        calls print_multi() on every instance of car in the class
        """
        if len(self.car_list) > 0:
            self.car_list[0].print_header()
            for car in self.car_list:
                car.print_multi()
