"""
CP1404 prac 6
languages.py (the client program)
estimate time:5 min
actual time:
"""
from prac_06.programming_language import ProgrammingLanguage
def main():
    """Demonstrate the use of the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # Test __str__ method
    print(python)