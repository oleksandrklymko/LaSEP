from category import Category
from product import Product
from shop import Shop
from provider import Provider
from customer import Customer
from datetime import datetime

store = Shop('24/7', 1000000)
alex = Customer('Alex', 50000)
fast_food = Category('Fast-food')
sweet = Category('Sweet')
hot_dog = Product('Hot dog', fast_food, 'g', '2020.12.1', 50, 100)
cake = Product('Cake', sweet, 'kg', '2021.1.12', 100, 200)
lidl = Provider('Lidl', 3000)
lidl.add_product(hot_dog, 10)
lidl.add_product(cake, 20)

store.buy_products(lidl, (cake, 10), (hot_dog, 10))
print(store.products)
print(lidl.products)

store.buy_products(lidl, (cake, 10))
print(store.products)

alex.buy_products(store, (hot_dog, 10))
print(alex.products)
print(store.products)

print('--------------------')

alex.buy_products(store, (cake, 10))
print(alex.products)
print(store.products)

print(store.purchase_history)
print(store.sales_history)


lidl.add_product(hot_dog, 200)
lidl.add_product(cake, 100)
store.buy_products(lidl, (cake, 100), (hot_dog, 200))


print(store.products)
store.show_products_with_category(fast_food)

store.show_all_providers()



