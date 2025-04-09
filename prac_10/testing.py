"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    car = Car(name="TestCar")
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(name="Test", fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when specified"

    default_car = Car(name="Default")
    assert default_car.fuel == 0, "Car does not set default fuel to 0"


run_tests()

doctest.testmod()

def phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.
    >>> phrase_as_sentence("hello")
    'Hello.'
    >>> phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_as_sentence("how are you")
    'How are you.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]