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
        self.street_name = street_name
        self.street_number = street_number
        # pylint: disable=C0103
        (self.left, self.right, self.up, self.down) = directions
        # pylint: enable=C0103
        self.traffic_lights = None
    # pylint: enable=W0102

    def print_header(self):
        """prints header for table print of Street objects
        """
        print "Street Name\t|\tStreet Number\t|\tLeft\t|\tRight\t|\tUp\t|\tDown"
        return self

    def print_multi(self):
        """prints all the data of Street object
        """
        print "%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s\t|\t%s" % \
        (self.street_name, self.street_number, self.left, self.right, self.up, self.down)
        return self

    def __repr__(self):
        return "%s %s" % (self.street_name, self.street_number)

    def get_all(self):
        """returns a table of all connected streets
        """
        return [self.up, self.right, self.down, self.left]

    def get_left(self):
        """returns street connected to the left
        """
        return self.left

    def get_right(self):
        """returns street connected to the right
        """
        return self.right

    def get_up(self):
        """returns street connected to the up
        """
        return self.up

    def get_down(self):
        """returns street connected to the down
        """
        return self.down

    def set_left_both(self, street_to_set):
        """sets current streets left to given one and given ones right to current street
        """
        street_to_set.set_right(self)
        self.set_left(street_to_set)
        return self

    def set_left(self, street_to_set):
        """sets current streets left to given one and also checks and sets lights if needed
        """
        self.left = street_to_set
        self.check_and_set_lights()

    def set_right_both(self, street_to_set):
        """sets current streets right to given one and given ones left to current street
        """
        street_to_set.set_left(self)
        self.set_right(street_to_set)
        return self

    def set_right(self, street_to_set):
        """sets current streets right to given one and also checks and sets lights if needed
        """
        self.right = street_to_set
        self.check_and_set_lights()

    def set_up_both(self, street_to_set):
        """sets current streets up to given one and given ones down to current street
        """
        street_to_set.set_down(self)
        self.set_up(street_to_set)
        return self

    def set_up(self, street_to_set):
        """sets current streets up to given one and also checks and sets lights if needed
        """
        self.up = street_to_set
        self.check_and_set_lights()

    def set_down_both(self, street_to_set):
        """sets current streets down to given one and given ones up to current street
        """
        street_to_set.set_up(self)
        self.set_down(street_to_set)
        return self

    def set_down(self, street_to_set):
        """sets current streets down to given one and also checks and sets lights if needed
        """
        self.down = street_to_set
        self.check_and_set_lights()

    def check_and_set_lights(self):
        """checks whether current road is connected to more than 2 streets and if the answer is yes
        setups new lights for current Street
        """
        if len([street for street in self.get_all if street is not None]) > 2:
            self.traffic_lights = TrLight.TrafficLight(street_parent=self)

    def get_lights(self):
        """return Streets TrafficLight
        """
        if self.traffic_lights == None:
            print(self, "This is not a crossroad, hence no lights to return!")
        return self.traffic_lights

    def is_crossroad(self):
        """returns True if Street has TrafficLight
        returns False otherwise
        """
        if self.traffic_lights == None:
            return False
        else:
            return True
