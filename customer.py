class Customer:
    # Initialise customer vars
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.rented_car = None

    # Returns string of customer vars
    def __str__(self):
        return f"{self.name} ({self.age})"

    # Sets if car is rented
    def rent_car(self, car):
        if car.rent():
            self.rented_car = car
            return True
        return False

    # Checks if car is rented & if True then returns car
    def return_car(self):
        car = self.rented_car
        if car is not None and car.return_car():
            self.rented_car = None
            return True
        return False
