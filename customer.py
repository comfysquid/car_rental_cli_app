class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.rented_car = None

    def __str__(self):
        return f"{self.name} ({self.age})"

    def rent_car(self, car):
        if car.rent():
            self.rented_car = car
            return True
        return False

    def return_car(self):
        car = self.rented_car
        if car is not None and car.return_car():
            self.rented_car = None
            return True
        return False
