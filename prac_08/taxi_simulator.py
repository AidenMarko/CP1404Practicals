"""
CP1404/CP5632 Practical
Taxi class
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    menu = """Q = Quit \nC = Choose Taxi\nD = Drive"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    taxi = ""
    current_bill = 0
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            taxi = choose_taxi(taxis)
        elif choice == "D":
            if taxi != "":
                cost = drive(taxi)
                current_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option")
        print("Your current bill is: ${:.2f}".format(current_bill))
        print(menu)
        choice = input(">>> ").upper()
    print("Thank You")

def choose_taxi(current_taxis):
    taxis = current_taxis
    i = 0
    print("Taxis available: ")
    for taxi in taxis:
        car = taxi
        print("{} - ".format(i), str(car))
        i += 1
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

def drive(taxi):
    distance = input("Drive how far? ")
    taxi.start_fare()
    taxi.drive(int(distance))
    print(taxi.get_fare())
    cost = int(taxi.get_fare()) * int(distance)
    print("Your {} trip cost you ${:.2f}".format(taxi.name, cost))
    return cost


main()
