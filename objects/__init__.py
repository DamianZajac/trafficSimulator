"""
objects module
contains 3 classes that define base logic for the application namely
Car, Street, TrafficLight
"""
import objects.car
print "Succesfully loaded Car"
import objects.street
print "Succesfully loaded Street"
import objects.traffic_light
print "Succesfully loaded TrafficLight"

def print_singular(given_object):
    """
    print_singular(Car/Street/TrafficLight obj) -> obj
    calls print_header and print_multi on given object
    returns same object
    """
    given_object.print_header()
    given_object.print_multi()
    return given_object
