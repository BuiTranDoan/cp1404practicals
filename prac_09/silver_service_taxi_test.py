from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare: ${fare:.2f}")
    assert fare == 48.8, f"Expected $48.80, got ${fare:.2f}"

if __name__ == "__main__":
    main()