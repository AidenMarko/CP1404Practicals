"""
CP1404/CP5632 Practical
Taxi class
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    menu = """Q = Quit \nC = Choose Taxi\nD = Drive"""
    current_bill = 0
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            taxi = choose_taxi()
        elif choice == "D":
            drive()
        else:
            print("Invalid Option")
        print(current_bill)
        print(menu)
        choice = input(">>> ").upper()
    print("Thank You")

def choose_taxi():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    i = 0
    for taxi in taxis:
        car = taxi
        print("{} - ".format(i), str(car))
        i += 1
    print("choose taxi")
    choice = input(">>> ")
    while choice != "":
        if choice == "0":
            return taxis[0]
        elif choice == "1":
            return taxis[1]
        elif choice == "2":
            return taxis[2]
        else:
            print("Invalid Option")

def drive():
    print("drive")


main()
