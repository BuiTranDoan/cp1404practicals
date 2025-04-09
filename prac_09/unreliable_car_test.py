from prac_09.unreliable_car import UnreliableCar

def test_unreliable_car():
    reliable_car = UnreliableCar("ReliableCar", 100, 100)
    unreliable_car = UnreliableCar("UnreliableCar", 100, 10)

    reliable_drive_total = 0
    unreliable_drive_total = 0

    # Try 100 drives for each car
    for i in range(100):
        reliable_drive_total += reliable_car.drive(1)
        unreliable_drive_total += unreliable_car.drive(1)
    print(f"Reliable car drove: {reliable_drive_total} km (expected ~100)")
    print(f"Unreliable car drove: {unreliable_drive_total} km (expected << 100)")

if __name__ == "__main__":
    test_unreliable_car()