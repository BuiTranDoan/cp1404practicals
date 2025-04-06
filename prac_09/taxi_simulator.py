from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Main function to simulate the taxi program."""
    taxis = [Taxi("Prius", 100),
    SilverServiceTaxi("Limo", 100, 2),
    SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None  # No taxi selected initially
    total_bill = 0
    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").strip().lower()
        if user_choice == 'q':
            quit_program(total_bill, taxis)
            break
        elif user_choice == 'c':
            current_taxi = choose_taxi(taxis)
            current_taxi.start_fare()
        elif user_choice == 'd':
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

def display_taxis(taxis):
    """Display available taxis to the user."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Allow the user to choose a taxi."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None

def drive_taxi(current_taxi, total_bill):
    """Allow the user to drive the selected taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        try:
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            fare = current_taxi.get_fare()
            total_bill += fare
            print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        except ValueError:
            print("Invalid input for distance.")
    return total_bill

def quit_program(total_bill, taxis):
    """Quit the program and display the final bill."""
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()