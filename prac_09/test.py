from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def choose_taxi(taxis):
    """Choose a taxi from the list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(current_taxi):
    """Drive the chosen taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return

    try:
        distance = int(input("Drive how far? "))
        distance_driven = current_taxi.drive(distance)

        # Calculate and display the fare if distance was driven
        if distance_driven > 0:
            fare = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        else:
            print(f"{current_taxi.name} has no fuel left!")

    except ValueError:
        print("Invalid input")


def taxi_simulator():
    """Main program to simulate taxi driving."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0

    while True:
        print(f"Bill to date: ${bill:.2f}")
        choice = input("q)uit, c)hoose taxi, d)rive: ").strip().lower()

        if choice == 'q':
            print(f"Total trip cost: ${bill:.2f}")
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            drive_taxi(current_taxi)
            bill += current_taxi.get_fare()  # Add the fare to the bill
        else:
            print("Invalid option")


# Run the taxi simulator
taxi_simulator()