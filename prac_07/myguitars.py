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

    guitars.extend(get_user_guitars())    # Allow user to enter new guitars


    save_guitars(FILENAME, guitars)    # Save updated list to file
    print("\nUpdated guitar list saved to file.")

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

def get_user_guitars():
    """Prompt the user to enter new guitars and return them as a list."""
    new_guitars = []
    while True:
        name = input("\nEnter guitar name (or press Enter to finish): ").strip()
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars

def save_guitars(filename, guitars):
    """Write the list of guitars to a file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

if __name__ == "__main__":
    main()