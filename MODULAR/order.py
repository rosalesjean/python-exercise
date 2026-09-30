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
        item = self.menu.get_item()
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
            print(
                f"{item:<35}"
                f"{quantity:>5}"
                f" ₱{item_total:>10.2f}"
            )

        print("-" * 60)

    def calculate_subtotal(self):
        subtotal = 0

        for item, quantity in self.items.items():
            subtotal += self.menu.items[item] * quantity

        return subtotal

    def calculate_discount(self, customer_type):
        subtotal = self.calculate_subtotal()

        if customer_type == "senior":
            return subtotal * 0.05

        return 0

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

            if choice == "2":
                return "senior"

            print("Invalid choice. Please enter 1 or 2.")