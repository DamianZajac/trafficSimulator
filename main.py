# coding=utf-8
"""
This is the Traffic Simulator, created by Kacper Stąpor, Damian Zając, Michał Zagól
It's a final project for Python Course at Jagiellonian University

2015
"""

#import objects
import generators
#import gui
#import core

if __name__ == "__main__":
    CAR_GEN = generators.car_generator.Car_Generator()
    i = 0
    CAR_LIST = []
    STREET_LIST = []
    print "==Street generator test=="
    STREET_GEN = generators.street_generator.Street_Generator()
    for STREET in STREET_GEN.get_street():
        STREET_LIST.append(STREET)
        STREET.print_multi()
        i += 1
        if i > 50:
            break
    print "==Car generator test(using previously generated streets)=="
    for CAR in CAR_GEN.get_car(STREET_LIST):
        CAR_LIST.append(CAR)
        CAR.print_multi()
        i += 1
        if i > 70:
            break
    print "==Street connections tests=="
    STREET_LIST[0].set_left_both(STREET_LIST[1]).set_right_both(STREET_LIST[2])
    STREET_LIST[0].set_down_both(STREET_LIST[3]).set_up_both(STREET_LIST[4]).print_singular()
    STREET_LIST[1].set_left_both(STREET_LIST[5]).set_up_both(STREET_LIST[6]).print_multi()
    print "==Lights on connected streets tests=="
    STREET_LIST[0].get_lights().switch_lights(15)
    STREET_LIST[1].get_lights().set_delays(5, 20).switch_lights(5)
    print "==Car movement over connected streets tests=="
    STREET_LIST[1].print_singular().get_lights().switch_lights(25).print_singular()
    CAR_LIST[0].set_position(STREET_LIST[1]).print_singular()
    CAR_LIST[0].move().print_singular().move().print_singular()
    