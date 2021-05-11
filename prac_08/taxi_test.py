"""
CP1404/CP5632 Practical
Taxi - Testing
"""

from prac_08.taxi import Taxi

def main():
    my_car = Taxi("Prius 1", 100)
    my_car.drive(40)
    print("Taxi: {}, Fare Distance: {}, Fare Cost: {}".format(my_car.name, my_car.current_fare_distance, my_car.
                                                              current_fare_distance * my_car.price_per_km))
    my_car.start_fare()
    my_car.drive(100)
    print("Taxi: {}, Fare Distance: {}, Fare Cost: {}".format(my_car.name, my_car.current_fare_distance, my_car.
                                                              current_fare_distance * my_car.price_per_km))


main()
