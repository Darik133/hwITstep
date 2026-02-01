class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"object '{product.name}' added successfully")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"object '{product_name}' deleted successfully")
                return
        print("Item not found in cart")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def show_cart(self):
        if not self.products:
            print("Кошик порожній")
        else:
            for product in self.products:
                print(f"{product.name} — {product.quantity} pieces. × {product.price} grn")
            print("Full price:", self.total_price())


# приклад використання
p1 = Product("Hot weels-car", 8000, 1)
p2 = Product("parfume", 1200, 2)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

cart.show_cart()
cart.remove_product("Hot weels-car")
cart.show_cart()
cart.show_cart()