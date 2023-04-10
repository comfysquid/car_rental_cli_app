from customer import Customer
from car import Car


class RentalService:
    # sets list of cars for rent and empty dicts of currently rented cars & customers
    def __init__(self):
        self.available_cars = [
            Car("Ford", "Focus", 2022),
            Car("Ford", "Mustang", 2021),
            Car("Ford", "Ranger", 2023),
            Car("Honda", "Civic", 2022),
            Car("Honda", "CR-V", 2021),
            Car("Honda", "HR-V", 2023),
            Car("Hyundai", "i30", 2022),
            Car("Hyundai", "Kona", 2021),
            Car("Hyundai", "Tucson", 2023),
            Car("Kia", "Cerato", 2022),
            Car("Kia", "Sorento", 2021),
            Car("Kia", "Sportage", 2023),
            Car("Mazda", "CX-5", 2022),
            Car("Mazda", "Mazda3", 2021),
            Car("Mazda", "MX-5", 2023),
            Car("Subaru", "Forester", 2022),
            Car("Subaru", "Outback", 2021),
            Car("Subaru", "XV", 2023),
            Car("Toyota", "Corolla", 2022),
            Car("Toyota", "HiLux", 2021),
            Car("Toyota", "Rav4", 2023),
            Car("Volkswagen", "Golf", 2022),
            Car("Volkswagen", "Polo", 2021),
            Car("Volkswagen", "Tiguan", 2023)
        ]
        self.rented_cars = []
        self.customers = []
        self.rented_cars = []
        self.customers = []

    def add_car(self, car):
        self.available_cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    # check if car exists & is available for rent
    def rent_car(self, customer_name, customer_age, car_make, car_model, car_year):
        car = self.find_car(car_make, car_model, car_year)
        if car is None or not car.is_available:
            return False
    # check if customer exists and isn't renting other cars, and then add cust if false
        customer = self.find_customer(customer_name)
        if customer is None:
            customer = Customer(customer_name, customer_age)
            self.add_customer(customer)

        if not customer.rent_car(car):
            return False

        car.rent()
        self.available_cars.remove(car)
        self.rented_cars.append(car)
        return True

    def return_car(self, customer_name):
        customer = self.find_customer(customer_name)
        if customer is None or customer.rented_car is None:
            return False

        car = customer.rented_car
        if not customer.return_car():
            return False

        car.return_car()
        self.available_cars.append(car)
        self.rented_cars.remove(car)
        return True

    def list_available_cars(self):
        return self.available_cars

    def list_rented_cars(self):
        return self.rented_cars

    def list_customers(self):
        return self.customers

    def find_car(self, make, model, year):
        for car in self.available_cars + self.rented_cars:
            if car.make == make and car.model == model and car.year == year:
                return car
        return None

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None
