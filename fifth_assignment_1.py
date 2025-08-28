#Part 1 of the assignment

class Smartphone:
    """A class to represent a smartphone with basic features."""

    def __init__(self, brand, model, storage, battery):
        # Initialize attributes
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in percentage
    
    def make_call(self, number):
        """Simulates making a phone call."""
        print(f"{self.model} is calling {number}... 📞")

    def charge(self, amount):
        """Charges the battery by a certain percentage."""
        self.battery = min(100, self.battery + amount)
        print(f"{self.model} charged. Battery: {self.battery}% 🔋")
    
    def check_storage(self):
        """Checks available storage."""
        print(f"{self.model} has {self.storage}GB of storage left.")


# Inheritance Example
class GamingPhone(Smartphone):
    """A subclass of Smartphone with extra gaming features."""

    def __init__(self, brand, model, storage, battery, refresh_rate):
        super().__init__(brand, model, storage, battery)
        self.refresh_rate = refresh_rate  # in Hz

    def play_game(self, game):
        """Simulates playing a game."""
        print(f"{self.model} is playing {game} at {self.refresh_rate}Hz!")
        self.battery -= 10  # drains battery
        print(f"Battery now at {self.battery}%")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 85)
phone1.make_call("071 2345 890")
phone1.charge(10)
phone1.check_storage()

