class Car:
    # Init car vars
    def __init__(self, make, model, year, is_available=True):
        self.make = make
        self.model = model
        self.year = year
        self.is_available = is_available

    # string of car vars
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    # check if available for rent
    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    # changes if car is available again
    def return_car(self):
        self.is_available = True
        return True
