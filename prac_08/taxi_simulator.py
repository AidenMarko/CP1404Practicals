"""
CP1404/CP5632 Practical
Taxi class
"""

from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    menu = """
    Q = Quit
    C = Choose Taxi
    D = Drive
    """
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            choose_taxi()
        elif choice == "D":
            drive()
        else:
            print("Invalid Option")

def choose_taxi():


def drive():


main()
