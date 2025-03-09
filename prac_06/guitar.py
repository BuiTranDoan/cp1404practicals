"""
CP1404 Prac 6 Guitar program
guitar.py, guitars.py and guitar_test.py
estimate time: 30min
actual time:
"""
from datetime import datetime

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, else False."""
        return self.get_age() >= 50