class Menu:
    def __init__(self):
        self.items = {
            "Chickenjoy with Rice": 99.00,
            "Jolly Spaghetti": 65.00,
            "Yumburger": 45.00,
            "Burger Steak": 75.00,
            "Chicken Sandwich": 85.00,
            "French Fries": 50.00,
            "Peach Mango Pie": 40.00,
            "Coca-Cola": 35.00,
            "Sprite": 35.00,
            "Royal": 35.00,
            "Iced Tea": 40.00
        }

    def display_menu(self):
        print("\n" + "=" * 60)
        print("                 JOLLIBITE EXPRESS")
        print("                     FULL MENU")
        print("=" * 60)
        print(f"{'NO.':<5} {'ITEM':<35} {'PRICE':>10}")
        print("-" * 60)

        for number, (item, price) in enumerate(self.items.items(), 1):
            print(f"{number:<5} {item:<35} ₱{price:>8.2f}")

        print("=" * 60)


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = {}

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity

                print("Quantity must be greater than 0.")

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

    def add_item(self):
        menu_items = list(self.menu.items.keys())

        while True:
            try:
                item_number = int(input("Enter item number: "))

                if 1 <= item_number <= len(menu_items):
                    item = menu_items[item_number - 1]
                    break

                print("Invalid item number. Please choose from the menu.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        quantity = self.get_quantity()

        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

        print(f"\nAdded {quantity} x {item} to your order.")

    def display_order(self):
        print("\n" + "-" * 60)
        print("                    CURRENT ORDER")
        print("-" * 60)
        print(f"{'ITEM':<35} {'QTY':>5} {'TOTAL':>12}")
        print("-" * 60)

        for item, quantity in self.items.items():
            item_total = self.menu.items[item] * quantity
            print(f"{item:<35} {quantity:>5} ₱{item_total:>10.2f}")

        print("-" * 60)

    def calculate_subtotal(self):
        subtotal = 0

        for item, quantity in self.items.items():
            subtotal += self.menu.items[item] * quantity

        return subtotal


class Receipt:
    def __init__(self, order):
        self.order = order

    def get_customer_type(self):
        print("\n" + "-" * 60)
        print("                    CUSTOMER TYPE")
        print("-" * 60)
        print("1. Regular Customer")
        print("2. Senior Citizen")
        print("-" * 60)

        while True:
            choice = input("Choose customer type (1/2): ").strip()

            if choice == "1":
                return "regular"

            elif choice == "2":
                return "senior"

            else:
                print("Invalid choice. Please enter 1 or 2.")

    def calculate_discount(self, customer_type):
        subtotal = self.order.calculate_subtotal()

        if customer_type == "senior":
            return subtotal * 0.05

        return 0

    def display_receipt(self, customer_type):
        subtotal = self.order.calculate_subtotal()
        discount = self.calculate_discount(customer_type)
        total = subtotal - discount

        print("\n")
        print("=" * 70)
        print("                      JOLLIBITE EXPRESS")
        print("                   OFFICIAL SALES RECEIPT")
        print("=" * 70)

        print(
            f"{'ITEM':<35}"
            f"{'QTY':>5}"
            f"{'PRICE':>10}"
            f"{'TOTAL':>12}"
        )

        print("-" * 70)

        for item, quantity in self.order.items.items():
            price = self.order.menu.items[item]
            item_total = price * quantity

            print(
                f"{item:<35}"
                f"{quantity:>5}"
                f" ₱{price:>8.2f}"
                f" ₱{item_total:>10.2f}"
            )

        print("-" * 70)
        print(f"{'SUBTOTAL':<55} ₱{subtotal:>10.2f}")
        print(f"{'CUSTOMER TYPE':<55} {customer_type.upper():>10}")

        if discount > 0:
            print(
                f"{'SENIOR CITIZEN DISCOUNT (5%)':<55}"
                f" -₱{discount:>9.2f}"
            )
        else:
            print(f"{'DISCOUNT':<55} ₱{discount:>10.2f}")

        print("-" * 70)
        print(f"{'TOTAL AMOUNT':<55} ₱{total:>10.2f}")
        print("=" * 70)
        print("                THANK YOU FOR ORDERING!")
        print("                   PLEASE COME AGAIN!")
        print("=" * 70)


def get_yes_no(message):
    while True:
        answer = input(message).strip().lower()

        if answer in ["yes", "y"]:
            return True

        elif answer in ["no", "n"]:
            return False

        else:
            print("Invalid input. Please enter Yes or No.")