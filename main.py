from rental_service import RentalService
from car import Car


def print_menu():
    print("Car Rental Service Menu")
    print("1. Add a car")
    print("2. Rent a car")
    print("3. Return a car")
    print("4. List available cars")
    print("5. List rented cars")
    print("6. List customers")
    print("0. Exit")


def main():
    rental_service = RentalService()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            car = Car(make, model, year)
            rental_service.add_car(car)
            print(f"{car} added to the available cars.")

        elif choice == "2":
            customer_name = input("Enter your name: ")
            customer_age = int(input("Enter your age: "))
            if customer_age < 18:
                print("You must be 18 or older to rent a car.")
                continue
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            success = rental_service.rent_car(customer_name, customer_age, make, model, year)
            if success:
                print(f"{customer_name} rented {make} {model} ({year}).")
            else:
                print(f"{make} {model} ({year}) is not available for rent.")

        elif choice == "3":
            customer_name = input("Enter your name: ")
            success = rental_service.return_car(customer_name)
            if success:
                print(f"{customer_name} returned the car.")
            else:
                print("You don't have any rented cars.")

        elif choice == "4":
            available_cars = rental_service.list_available_cars()
            if available_cars:
                print("Available cars:")
                for car in available_cars:
                    print(f"- {car}")
            else:
                print("There are no available cars at the moment.")

        elif choice == "5":
            rented_cars = rental_service.list_rented_cars()
            if rented_cars:
                print("Rented cars:")
                for car in rented_cars:
                    print(f"- {car}")
            else:
                print("There are no rented cars at the moment.")

        elif choice == "6":
            customers = rental_service.list_customers()
            if customers:
                print("Customers:")
                for customer in customers:
                    print(f"- {customer}")
            else:
                print("There are no customers at the moment.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")

    print("Thank you for using our Car Rental Service!")


if __name__ == "__main__":
    main()