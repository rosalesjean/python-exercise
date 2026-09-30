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

    def get_item(self):
        menu_items = list(self.items.keys())

        while True:
            try:
                item_number = int(input("Enter item number: "))

                if 1 <= item_number <= len(menu_items):
                    return menu_items[item_number - 1]

                print("Invalid item number. Please choose from the menu.")

            except ValueError:
                print("Invalid input. Please enter a number.")