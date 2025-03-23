"""
Prac 07 - More Guitars
Reads guitars from a file, displays them, allows user to add new guitars, then saves back to file.
"""
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Main function to manage guitars."""
    guitars = load_guitars(FILENAME)

    print("Guitars from file:")
    display_guitars(guitars)

    guitars.sort()    # Sort guitars by year
    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

def load_guitars(filename):
    """Read guitars from a file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display the list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")