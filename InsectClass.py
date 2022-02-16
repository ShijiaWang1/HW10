import random


class Insect:
    def __init__(self, wings, legs):
        self.wings = wings
        self.legs = legs
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1, 10)

    def get_miles(self):
        return self.flight
