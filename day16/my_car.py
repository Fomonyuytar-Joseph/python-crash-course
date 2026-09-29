from car import Car

my_new_car = Car('toyota', 'rav4', 2026)


print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 21000
my_new_car.update_odometer(3000)
my_new_car.increment_odometer(500)
my_new_car.read_odometer()
