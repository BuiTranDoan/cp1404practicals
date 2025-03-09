"""
CP1404 Prac 6 Guitar program
guitar.py, guitars.py and guitar_test.py
estimate time: 30min
actual time:
"""
from guitar import Guitar


def main():
    """Manage and display a collection of guitars."""
    print("My guitars!")
    guitars = [
        Guitar("Gibson L-5 CES", 1922, 16035.40),
        Guitar("Line 6 JTV-59", 2010, 1512.90),
        Guitar("Fender Stratocaster", 2014, 765.40)
    ]
    # Display all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()