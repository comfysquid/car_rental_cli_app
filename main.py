from rental_service import RentalService
from menu import \
    print_menu, \
    add_car_menu, \
    rent_car_menu, \
    return_car_menu, \
    list_available_cars_menu, \
    list_rented_cars_menu, \
    list_customers_menu


def main():
    rental_service = RentalService()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_car_menu(rental_service)
            case "2":
                rent_car_menu(rental_service)
            case "3":
                return_car_menu(rental_service)
            case "4":
                list_available_cars_menu(rental_service)
            case "5":
                list_rented_cars_menu(rental_service)
            case "6":
                list_customers_menu(rental_service)
            case "0":
                break
            case _:
                print("Invalid choice. Try again.")

    print("Thank you for using our Car Rental Service!")


if __name__ == "__main__":
    main()
