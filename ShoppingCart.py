class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def summary(self):
        print(">>> Shopping Cart Contents <<<")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ KSH {price:.3f} each")
        print(f"Total: KSH {self.calculate_total():.3f}\n")



if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Kiwi", 50, 85)
    cart.add_item("Polisher", 50, 27)
    cart.add_item("Avocado", 100, 20)
    cart.add_item("Charcoal", 200, 15)

    print(">>> Regular Cart <<<")
    cart.summary()
