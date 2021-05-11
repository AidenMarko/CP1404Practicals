"""
CP1404/CP5632 Practical
Silver Service Taxi - Testing
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

car1 = SilverServiceTaxi("Hummer", 200, 2)
print(str(car1))
car1.drive(18)
print(str(car1))
print(car1.get_fare())
