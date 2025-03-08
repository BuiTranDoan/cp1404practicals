"""
CP1404 prac 6
programming_language.py (the class)
estimate time:15 min
actual time:
"""
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year