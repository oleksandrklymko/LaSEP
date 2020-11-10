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

    def buy_products(self, provider, date=datetime.today(), *args):
        bought_products = buy_products(self, provider, *args)
        if bought_products:
            information = (len(self.purchase_history) + 1, str(date), bought_products)
            if provider not in self.providers:
                self.providers[provider] = [information]
            else:
                self.providers[provider].append(information)
            self.purchase_history.append((len(self.purchase_history) + 1, provider, date, bought_products))
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

    def show_information_for_period(self, date_of_start, date_of_end):
        products = {}
        ordered_in_period = {}
        sold_in_period = {}

        for time_temp in self.purchase_history:
            date = time_temp[2]
            products_in_time_temp = time_temp[3]
            if date_of_start > date:
                for product, quantity in products_in_time_temp.items():
                    if product in products:
                        products[product] += quantity
                    else:
                        products[product] = quantity
            if date_of_start <= date <= date_of_end:
                for product, quantity in products_in_time_temp.items():
                    if product in ordered_in_period:
                        ordered_in_period[product] += quantity
                    else:
                        ordered_in_period[product] = quantity

        for time_temp in self.sales_history:
            date = time_temp[1]
            products_in_time_temp = time_temp[2]
            if date_of_start > date:
                for product, quantity in products_in_time_temp.items():
                    products[product] -= quantity
            if date_of_start <= date <= date_of_end:
                for product, quantity in products_in_time_temp.items():
                    if product in sold_in_period:
                        sold_in_period[product] += quantity
                    else:
                        sold_in_period[product] = quantity

        with open('report.txt', 'w') as file:
            file.write('At the begin of period we have: ')
            for product, quantity in products.items():
                file.write(f'\n\t{product} - {quantity}')

            file.write('\nWhile period we order: ')
            for product, quantity in ordered_in_period.items():
                file.write(f'\n\t{product} - {quantity}')

            file.write('\nWhile period we sold: ')
            for product, quantity in sold_in_period.items():
                file.write(f'\n\t{product} - {quantity}')
