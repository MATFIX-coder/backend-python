class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

class Customer:
    def __init__(self, name_profile):
        self.name_profile = name_profile
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        if product in self.items:
            self.items[product] = quantity

    def sum_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

class Order:
    def __init__(self, customer, cart, discount, tax):
        self.customer = customer
        self.items = cart.items.copy()
        self.sum_total = cart.sum_total()
        self.discount = discount
        self.tax = tax

    def calculate_total(self):
        total =  self.sum_total - ((self.sum_total * self.discount) / 100)
        return total + ((total * self.tax) / 100)

    def process(self):
        for product, quantity in self.items.items():
            product.stock -= quantity
        self.customer.add_order(self)