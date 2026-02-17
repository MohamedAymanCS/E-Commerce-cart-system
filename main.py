class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity: int) -> None:
        if quantity > self.stock:
            raise ValueError(f"Not enough stock available for {self.name}.")
        self.stock -= quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        product.reduce_stock(quantity)
        self.items.append((product, quantity))
        print(f"{product.name} added successfully.")

    def total_price(self) -> float:
        return sum(product.price * quantity for product, quantity in self.items)

    def cart_details(self) -> None:
        print("\n========== CART ==========")

        if not self.items:
            print("Your cart is empty.")
        else:
            for product, quantity in self.items:
                print(f"{product.name}: {quantity} x {product.price} = {product.price * quantity}")

            print("--------------------------")
            print(f"Total: {self.total_price()}")

        print("==========================\n")


if __name__ == "__main__":
    product1 = Product("iPhone", 70000, 15)
    product2 = Product("Laptop", 30000, 20)

    cart = Cart()
    cart.add_product(product1, 4)
    cart.add_product(product2, 8)

    cart.cart_details()
