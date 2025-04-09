class Band:
    """Band class to manage a list of musicians."""

    def __init__(self, name):
        """Initialize the band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band with its musicians and their instruments."""
        band_info = f"{self.name} "
        musician_info = [f"{musician.name} ({', '.join(str(instrument) for instrument in musician.instruments)})" for musician in self.musicians]
        band_info += "(".join(musician_info) + ")"
        return band_info

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string representing the performance of each musician in the band."""
        performance = []
        for musician in self.musicians:
            if musician.instruments:
                performance.append(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                performance.append(f"{musician.name} needs an instrument!")
        return "\n".join(performance)