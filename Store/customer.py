from module import buy_products, add_product
from datetime import datetime

class Customer:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.products = {}

    def __repr__(self):
        return self.name

    def buy_products(self, shop, *args, date=datetime.today()):
        bought_products = buy_products(self, shop, *args)
        if bought_products:
            shop.sales_history.append((len(shop.sales_history)+1, str(date.date()), bought_products))

