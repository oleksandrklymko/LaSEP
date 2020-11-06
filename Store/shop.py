from module import buy_products
from datetime import datetime


class Shop:

    def __init__(self, title, money):
        self.title = title
        self.products = {}
        self.money = money
        self.sales_history = []
        self.purchase_history = []
        self.providers = {}

    def buy_products(self, provider, *args, date=datetime.today()):
        bought_products = buy_products(self, provider, *args)
        if bought_products:
            information = (len(self.purchase_history) + 1, str(date.date()), bought_products)
            if provider not in self.providers:
                self.providers[provider] = [information]
            else:
                self.providers[provider].append(information)
            self.purchase_history.append((len(self.purchase_history) + 1, provider, str(date.date()), bought_products))
        return False

    def show_products_with_category(self, category):
        products = [product for product in self.products if product.category == category]
        if products:
            print(category)
            for product in products:
                print(f'Product: {product}, Purchase price: {product.purchase_price}', end=' ')
                print(f'Selling price: {product.selling_price}, Available quantity: {self.products[product]}')
        return False

    def show_all_providers(self):
        for provider in self.providers:
            print(provider, end=': \n')
            for document in self.providers[provider]:
                print(document)
