from generators import street_generator as str_gen, car_generator as car_gen

class Game:
    def __init__(self, os = "WIN32", street_number = 1, car_number = 1):
        self.street_gen = str_gen.Street_Generator()
        self.car_gen = car_gen.Car_Generator()
        self.os = os
        self.street_list = [self.street_gen.get_street()]
        self.car_list = []
        self.timer = 0
        
    def run(self):
        if self.os == "WIN32":
            timer += 1
            move_cars()
            
        else:
            pass
            
    def move_cars(self):        
        for car in car_list:
            pass
            
    def check_lights(self):
        for street in self.street_list:
            if street.is_crossroad:
                street.get_lights.switch_lights(timer)
                
    def set_street_list(self, street_list):
        self.street_list = street_list
        
    def set_car_list(self, car_list):
        self.car_list = car_list