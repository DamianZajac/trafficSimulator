import objects
import core
import generators
import gui

if(__name__ == "__main__"):
	car1 = objects.car.Car()
	car1.print_singular()
	car2 = objects.car.Car("Adam Adamicki", "Chinatown 1", "TKN 46FK")
	car2.print_singular()
	print
	objects.car.Car().print_header()
	car1.print_multi()
	car2.print_multi()
	
	street1 = objects.street.Street("Wadowicka", 1)
	street1.print_singular()
	street2 = objects.street.Street("Felinskiego", 33)
	street2.print_singular()
	print
	street1.set_down_both(street2).print_header().print_multi()
	street2.print_multi()
	
	car_gen = generators.car_generator.Car_Generator()
	
	car_list = []
	car1.print_header()
	i = 0
	
	for car in car_gen.get_car(["Wadowicka 1", "Felinskiego 33"]):
		car_list.append(car)
		car.print_multi()
		i += 1
		if i > 20:
			break
			
	street_list = []
	street1.print_header()
	street_gen = generators.street_generator.Street_Generator()
	
	for street in street_gen.get_street():
		street_list.append(street)
		street.print_multi()
		i += 1
		if i > 50:
			break
			
	street_list[0].set_left_both(street_list[1]).set_right_both(street_list[2]).set_down_both(street_list[3]).set_up_both(street_list[4])
	
	street_list[0].print_singular()
	street_list[0].get_lights().print_singular().switch_lights().print_singular()
	street_list[1].get_lights().print_singular()