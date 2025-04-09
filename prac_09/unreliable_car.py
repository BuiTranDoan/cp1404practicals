import random
from prac_09.car import Car

class UnreliableCar(Car):
    """An unreliable car that only sometimes drives."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability
    def drive(self, distance):
        """Drive the car only if it's reliable enough this time."""
        chance = random.uniform(1,100)
        if chance < self.reliability:
            # Car drives normally
            return super().drive(distance)
        else:
            # Car fails to drive
            return 0

