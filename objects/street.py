"""
street module
contains Street class implementation
"""
import objects.traffic_light as TrLight

class Street(object):
    """
    Street class
    class that implements Street object
    it has its own street name as well as number
    it has 4 nodes to adjacent streets
    it has its own TrafficLight if it is a crossroad
    """
    # pylint: disable=W0102
    def __init__(self, street_name, street_number, directions=[None, None, None, None]):
        self.street_name = street_name + str(street_number)
        # pylint: disable=C0103
        (self.left, self.right, self.up, self.down) = directions
        # pylint: enable=C0103
        self.traffic_lights = None
        self.car_list = []
    # pylint: enable=W0102

    def print_header(self):
        """prints header for table print of Street objects
        """
        print "Street Name and Number\t|\tLeft\t|\tRight\t|\tUp\t|\tDown"
        return self

    def print_multi(self):
        """prints all the data of Street object
        """
        print "%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s" % \
        (self.street_name, self.left, self.right, self.up, self.down)
        return self

    def __repr__(self):
        return "%s %d" % (self.street_name, len(self.car_list))

    def get_all(self):
        """returns a table of all connected streets
        """
        return [self.up, self.right, self.down, self.left]

    def set_left_both(self, street_to_set):
        """sets current streets left to given one and given ones right to current street
        """
        street_to_set.right = self
        self.left = street_to_set
        self.check_and_set_lights()
        street_to_set.check_and_set_lights()
        return self

    def set_right_both(self, street_to_set):
        """sets current streets right to given one and given ones left to current street
        """
        street_to_set.left = self
        self.right = street_to_set
        self.check_and_set_lights()
        street_to_set.check_and_set_lights()
        return self

    def set_up_both(self, street_to_set):
        """sets current streets up to given one and given ones down to current street
        """
        street_to_set.down = self
        self.up = street_to_set
        self.check_and_set_lights()
        street_to_set.check_and_set_lights()
        return self

    def set_down_both(self, street_to_set):
        """sets current streets down to given one and given ones up to current street
        """
        street_to_set.up = self
        self.down = street_to_set
        self.check_and_set_lights()
        street_to_set.check_and_set_lights()
        return self

    def check_and_set_lights(self):
        """checks whether current road is connected to more than 2 streets and if the answer is yes
        setups new lights for current Street
        """
        if len([street for street in self.get_all() if street is not None]) > 2:
            self.traffic_lights = TrLight.TrafficLight(street_parent=self)

    def is_crossroad(self):
        """returns True if Street has TrafficLight
        returns False otherwise
        """
        return self.traffic_lights != None

    def remove_car(self, car):
        """removes car from car_list
        returns self
        """
        self.car_list.remove(car)
        return self

    def add_car(self, car):
        """adds a car to car_list
        returns self
        """
        self.car_list.append(car)
        return self
