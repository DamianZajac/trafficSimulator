# coding=utf-8
"""
This is the Traffic Simulator, created by Kacper Stąpor, Damian Zając, Michał Zagól
It's a final project for Python Course at Jagiellonian University

2015
"""

#import objects
import generators
#import gui
import core
from random import choice

if __name__ == "__main__":
    CAR_GEN = generators.car_generator.CarGenerator()
    i = 0
    CAR_LIST = []
    STREET_LIST = []
    print "==Street generator test=="
    STREET_GEN = generators.street_generator.StreetGenerator()
    for STREET in STREET_GEN.get_street():
        STREET_LIST.append(STREET)
        STREET.print_multi()
        i += 1
        if i > 19:
            break
    i = 0
    print "==Car generator test(using previously generated streets)=="
    for car in CAR_GEN.get_car():
        CAR_LIST.append(car)
        car.print_multi()
        car.set_position(choice(STREET_LIST))
        car.set_destination(choice(STREET_LIST))
        i += 1
        if i > 4:
            break
    print "==Street connections tests=="
    STREET_LIST[0].set_right_both(STREET_LIST[1]).set_up_both(STREET_LIST[10])
    STREET_LIST[2].set_up_both(STREET_LIST[1]).set_down_both(STREET_LIST[11])
    STREET_LIST[3].set_left_both(STREET_LIST[1]).set_right_both(STREET_LIST[4])
    STREET_LIST[14].set_down_both(STREET_LIST[13]).set_up_both(STREET_LIST[4])
    STREET_LIST[5].set_down_both(STREET_LIST[4]).set_up_both(STREET_LIST[6])
    STREET_LIST[6].set_left_both(STREET_LIST[7]).set_up_both(STREET_LIST[15])
    STREET_LIST[6].set_right_both(STREET_LIST[12])
    STREET_LIST[16].set_left_both(STREET_LIST[15]).set_right_both(STREET_LIST[17])
    STREET_LIST[18].set_up_both(STREET_LIST[17]).set_left_both(STREET_LIST[12])
    STREET_LIST[18].set_down_both(STREET_LIST[19])
    STREET_LIST[8].set_right_both(STREET_LIST[7]).set_left_both(STREET_LIST[9])
    STREET_LIST[10].set_up_both(STREET_LIST[9])
    for street in STREET_LIST:
        tab = [x for x in street.get_all() if x is not None]
        print street, tab
    NEW_GAME = core.game.Game()
    NEW_GAME.set_street_list(STREET_LIST)
    NEW_GAME.create_cars(5)
    NEW_GAME.run()
    