from datetime import datetime


def add_product(customer, product, quantity):
    if product in customer.products:
        customer.products[product] += quantity
        return True
    customer.products[product] = quantity
    return True


def buy_products(customer, seller, *args, credit_limit=-1000):
    bought_products = {}
    for product, quantity in args:
        if product in seller.products:
            if customer.money >= credit_limit:
                new_available_quantity = seller.products[product] - quantity
                if new_available_quantity <= 0:
                    bought_product_quantity = seller.products[product]
                    seller.products.pop(product, None)
                else:
                    bought_product_quantity = seller.products[product] - new_available_quantity
                    seller.products[product] = new_available_quantity

                bought_products[product] = bought_product_quantity
                price = bought_product_quantity * product.selling_price
                customer.money -= price
                seller.money += price
                add_product(customer, product, bought_product_quantity)

    return bought_products
