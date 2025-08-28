# Activity 2: Polymorphism Challenge 

class Vehicle:
    """Base class for different types of vehicles."""
    def move(self):
        """Placeholder method to be overridden by subclasses."""
        print("This vehicle moves in its own way.")


class Car(Vehicle):
    def move(self):
        print("Driving on the road!")


class Plane(Vehicle):
    def move(self):
        print("Flying through the sky!")


class Boat(Vehicle):
    def move(self):
        print("Sailing on water!")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move() 
