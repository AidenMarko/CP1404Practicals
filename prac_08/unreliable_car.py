"""
CP1404/CP5632 Practical
Unreliable Car
"""
from prac_08.car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven