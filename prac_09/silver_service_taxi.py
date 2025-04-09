from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A special taxi with fanciness and a flagfall charge."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip, rounded to nearest 10c."""
        return round(self.price_per_km * self.current_fare_distance + self.flagfall, 1)

    def __str__(self):
        """Return string representation of the taxi with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"