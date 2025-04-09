from prac_09.taxi import Taxi

# Create a new taxi
my_taxi = Taxi("Prius 1", 100)

my_taxi.drive(40) # Drive 40 km
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

my_taxi.start_fare()
my_taxi.drive(100) # Restart fare and drive 100 km
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")