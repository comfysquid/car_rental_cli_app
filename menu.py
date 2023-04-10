from car import Car, Make


def print_menu():
    print("Car Rental Service Menu")
    print("1. Add a car")
    print("2. Rent a car")
    print("3. Return a car")
    print("4. List available cars")
    print("5. List rented cars")
    print("6. List customers")
    print("0. Exit")


def add_car_menu(rental_service):
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    if make not in Make.__members__:
        print("Invalid make.")
        return
    if model not in Make[make].value:
        print("Invalid model for this make.")
        return
    car = Car(make, model, year)
    rental_service.add_car(car)
    print(f"{car} added to the available cars.")


def rent_car_menu(rental_service):
    customer_name = input("Enter your name: ")
    customer_age = int(input("Enter your age: "))
    if customer_age < 18:
        print("You must be 18 or older to rent a car.")
        return
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    success = rental_service.rent_car(customer_name, customer_age, make, model, year)
    if success:
        print(f"{customer_name} rented {make} {model} ({year}).")
    else:
        print(f"{make} {model} ({year}) is not available for rent.")


def return_car_menu(rental_service):
    customer_name = input("Enter your name: ")
    success = rental_service.return_car(customer_name)
    if success:
        print(f"{customer_name} returned the car.")
    else:
        print("You don't have any rented cars.")


def list_available_cars_menu(rental_service):
    available_cars = rental_service.list_available_cars()
    if available_cars:
        print("Available cars:")
        for car in available_cars:
            print(f"- {car}")
    else:
        print("There are no available cars at the moment.")


def list_rented_cars_menu(rental_service):
    rented_cars = rental_service.list_rented_cars()
    if rented_cars:
        print("Rented cars:")
        for car in rented_cars:
            print(f"- {car}")
    else:
        print("There are no rented cars at the moment.")


def list_customers_menu(rental_service):
    customers = rental_service.list_customers()
    if customers:
        print("Customers:")
        for customer in customers:
            print(f"- {customer}")
    else:
        print("There are no customers at the moment.")