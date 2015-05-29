import objects
import core
import generators


if(__name__ == "__main__"):
	car1 = objects.car.Car()
	car1.print_singular()
	car2 = objects.car.Car("Ferrari 430", "Chinatown 1", "TKN 46FK")
	car2.print_singular()
	print
	objects.car.Car().print_header()
	car1.print_multi()
	car2.print_multi()
	
	street1 = objects.street.Street("Wadowicka", 1)
	street1.print_singular()
	street2 = objects.street.Street("Felinskiego", 33, left = "Wadowicka 1")
	street2.print_singular()
	print
	street1.print_header()
	street1.print_multi()
	street2.print_multi()