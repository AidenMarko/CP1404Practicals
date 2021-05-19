"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""

from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        """self.get_fare = Taxi.current_fare_distance * self.price_per_km + 4.50"""

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return super().get_fare() + 4.50
