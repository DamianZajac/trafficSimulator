# coding=utf-8
"""
This is the Traffic Simulator, created by Kacper Stąpor, Damian Zając, Michał Zagól
It's a final project for Python Course at Jagiellonian University

2015
"""

import objects
import generators
#import gui
#import core

if __name__ == "__main__":
    STREET1 = objects.street.Street("Wadowicka", 1)
    STREET1.print_singular()
    STREET2 = objects.street.Street("Felinskiego", 33)
    STREET2.print_singular()
    print
    STREET1.set_down_both(STREET2).print_header().print_multi()
    STREET2.print_multi()
    CAR1 = objects.car.Car(u"Karol Złoty", STREET1)
    CAR1.print_singular()
    CAR2 = objects.car.Car("Adam Adamicki", STREET2, "TKN 46FK")
    CAR2.print_singular()
    print
    CAR1.print_singular()
    CAR2.print_multi()
    CAR_GEN = generators.car_generator.Car_Generator()
    CAR_LIST = []
    CAR1.print_header()
    i = 0
    STREET_LIST = []
    STREET1.print_header()
    STREET_GEN = generators.street_generator.Street_Generator()
    for STREET in STREET_GEN.get_street():
        STREET_LIST.append(STREET)
        STREET.print_multi()
        i += 1
        if i > 50:
            break
    for CAR in CAR_GEN.get_car(STREET_LIST):
        CAR_LIST.append(CAR)
        CAR.print_multi()
        i += 1
        if i > 70:
            break
    STREET_LIST[0].set_left_both(STREET_LIST[1]).set_right_both(STREET_LIST[2])
    STREET_LIST[0].set_down_both(STREET_LIST[3]).set_up_both(STREET_LIST[4])
    STREET_LIST[1].set_left_both(STREET_LIST[5]).set_up_both(STREET_LIST[6])
    STREET_LIST[0].get_lights().switch_lights(15)
    STREET_LIST[1].get_lights().set_delays(5, 20).switch_lights(5)
    print
    STREET_LIST[1].print_singular()
    CAR_LIST[0].set_position(STREET_LIST[1]).print_singular()
    print
    CAR_LIST[0].move().print_singular().move().print_singular().move().print_singular()
    