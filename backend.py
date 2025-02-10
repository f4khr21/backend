class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_product(self):
        return f"{self.name} - ${self.price}"


class Cart:
    def __init__(self):
        self.items = []
    
    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")
    
    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your shopping cart has:")
            for item in self.items:
                print(f"- {item.display_product()}")
    
    def total_price(self):
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
    
    def add_to_cart(self, product):
        self.cart.add_product(product)
    
    def view_cart(self):
        self.cart.view_cart()
    
    def place_order(self):
        if not self.cart.items:
            print("You can't place an order while  cart is empty.")
            return None
        return Order(self)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = customer.cart.items.copy()
        print("Order placed successfully!")
        self.create_receipt()
    
    def create_receipt(self):
        print("Receipt")
        print("-" * 20)
        print(f"Customer: {self.customer.name}")
        print("Products:")
        for item in self.items:
            print(f"{item.display_product()}")
        print("Total: $", self.customer.cart.total_price())
        print("-" * 20)



if __name__ == "__main__":
    top = Product("Top", 20)
    jeans= Product("Jeans", 40)
    sweatpants = Product("sweatpants", 60)
    short = Product("short", 20)
    
    customer = Customer("f4khr")
    customer.add_to_cart(top)
    customer.add_to_cart(jeans)
    customer.add_to_cart(sweatpants)
    customer.add_to_cart(short)
    customer.view_cart()
    
    order = customer.place_order()
