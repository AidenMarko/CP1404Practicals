"""
CP1404/CP5632 Practical
Unreliable Car - Testing
"""

from prac_08.unreliable_car import UnreliableCar

def main():
    car1 = UnreliableCar("Car 1", 100, 100)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)
    car1.drive(10)
    print(car1.odometer)


main()
