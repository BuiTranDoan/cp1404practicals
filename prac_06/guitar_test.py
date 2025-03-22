"""
CP1404 Prac 6 Guitar program
guitar.py, guitars.py and guitar_test.py
estimate time: 30min
actual time: 27min
"""
from prac_06.guitar import Guitar

def test_guitar():
    """Test the Guitar class methods get_age() and is_vintage()."""

    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 765.40)
    # Testing get_age()
    print(f"{guitar1.name} get_age() - Expected {2025 - 1922}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {2025 - 2013}. Got {guitar2.get_age()}")
    # Testing is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


# Run the test function
test_guitar()