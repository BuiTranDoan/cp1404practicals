"""
CP1404 prac 6
languages.py (the client program)
estimate time:15 min
actual time: 23 min
"""
from prac_06.programming_language import ProgrammingLanguage
def main():
    """Demonstrate the use of the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # Test __str__ method
    print(python)
    # Store languages in a list
    languages = [python, ruby, visual_basic]
    # Print dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()