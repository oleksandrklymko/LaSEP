from module import buy_products
from datetime import datetime

class Customer:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.products = {}

    def __repr__(self):
        return self.name

    def buy_products(self, shop, date=datetime.today(), *args, ):
        bought_products = buy_products(self, shop, *args)
        if bought_products:
            shop.sales_history.append((len(shop.sales_history)+1, date, bought_products))

