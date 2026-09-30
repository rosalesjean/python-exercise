from menu import Menu
from order import Order
from receipt import Receipt


def get_yes_no(message):
    while True:
        answer = input(message).strip().lower()

        if answer in ["yes", "y"]:
            return True

        if answer in ["no", "n"]:
            return False

        print("Invalid input. Please enter Yes or No.")


def main():
    menu = Menu()
    order = Order(menu)
    receipt = Receipt(order)

    print("\n" + "=" * 60)
    print("                WELCOME TO JOLLIBITE EXPRESS")
    print("              YOUR FAVORITE FAST FOOD!")
    print("=" * 60)

    menu.display_menu()

    wants_to_order = get_yes_no(
        "\nWould you like to order? (Yes/No): "
    )

    if not wants_to_order:
        print("\nThank you for visiting Jollibite Express!")
        print("Have a great day!")
        return

    while True:
        menu.display_menu()

        order.add_item()
        order.display_order()

        another_item = get_yes_no(
            "\nWould you like to order another item? (Yes/No): "
        )

        if not another_item:
            break

    customer_type = order.get_customer_type()

    receipt.display(customer_type)


if __name__ == "__main__":
    main()