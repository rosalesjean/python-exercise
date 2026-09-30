from jollibite import Menu, Order, Receipt, get_yes_no


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

    customer_type = receipt.get_customer_type()

    receipt.display_receipt(customer_type)


if __name__ == "__main__":
    main()