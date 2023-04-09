class Car:
    def __init__(self, make, model, year, is_available=True):
        self.make = make
        self.model = model
        self.year = year
        self.is_available = is_available

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_car(self):
        self.is_available = True
        return True
