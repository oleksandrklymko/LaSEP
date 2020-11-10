from module import add_product

class Provider:

    def __init__(self, title, money):
        self.title = title
        self.products = {}
        self.money = money

    def __repr__(self):
        return self.title

    def add_product(self, product, quantity):
        add_product(self, product, quantity)
