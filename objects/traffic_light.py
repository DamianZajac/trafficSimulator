"""
traffic_light module
contains TrafficLight class implementation
"""

class TrafficLight(object):
    """
    TrafficLight class
    implements TrafficLight object base logic
    it contains street that it belongs to
    it contains delays for both horizontal and vertical lights
    it contains status of both horizontal and vertical lights
    """
    GREEN = True
    RED = False

    def __init__(self, street_parent, switch_delay_horizontal=5, switch_delay_vertical=5):
        self.street_parent = street_parent
        self.horizontal_light = TrafficLight.GREEN
        self.vertical_light = TrafficLight.RED
        self.switch_delay_horizontal = switch_delay_horizontal
        self.switch_delay_vertical = switch_delay_vertical

    def __repr__(self):
        return "Lights on", self.street_parent, "street :\nHorizontal:", \
        self.horizontal_light, " Vertical:", self.vertical_light

    def print_header(self):
        """prints header of TrafficLight object with names of data its print_multi method prints
        returns itself
        """
        print "Street Parent\t|\tHorizontal\t|\tVertical"
        return self

    def print_multi(self):
        """prints table like data of current TrafficLight
        """
        print "%s\t|\t%s %s\t|\t%s %s" % (self.street_parent, self.horizontal_light, \
            self.switch_delay_horizontal, self.vertical_light, self.switch_delay_vertical)
        return self

    def switch_lights(self, timer):
        """switches lights depending on if the timer meets the delay timers
        """
        help_timer = timer
        if help_timer == 0:
            help_timer = self.switch_delay_vertical + self.switch_delay_horizontal
        while help_timer > 0:
            help_timer -= self.switch_delay_horizontal
            help_timer -= self.switch_delay_vertical
        if help_timer == 0:
            print "Successfully switched lights (horizontal ON)"
            self.horizontal_light = TrafficLight.GREEN
            self.vertical_light = TrafficLight.RED
        else:
            if help_timer + self.switch_delay_vertical == 0:
                print "Successfully switched lights (vertical ON)"
                self.horizontal_light = TrafficLight.RED
                self.vertical_light = TrafficLight.GREEN
        return self

    def set_delay_horizontal(self, switch_delay):
        """sets delay of horizontal light
        returns itself
        """
        self.switch_delay_horizontal = switch_delay
        return self

    def set_delay_vertical(self, switch_delay):
        """sets delay of vertical light
        returns itself
        """
        self.switch_delay_vertical = switch_delay
        return self

    def set_delays(self, horizontal, vertical):
        """sets delay of horizontal and vertical lights
        returns itself
        """
        self.set_delay_horizontal(horizontal)
        self.set_delay_vertical(vertical)
        return self
