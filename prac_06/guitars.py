"""
CP1404 Prac 6 Guitar program
guitar.py, guitars.py and guitar_test.py
estimate time: 30min
actual time:
"""
from guitar import Guitar


def main():
    """Collect and display a list of guitars from user input."""

    print("My guitars!")
    guitars = []

    # Get user input
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    # Display all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()