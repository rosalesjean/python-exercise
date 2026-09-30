class Receipt:
    def __init__(self, order):
        self.order = order

    def display(self, customer_type):
        subtotal = self.order.calculate_subtotal()
        discount = self.order.calculate_discount(customer_type)
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