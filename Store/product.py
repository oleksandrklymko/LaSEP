class Product:
    product_id = 1

    def __init__(self, title, category, unit, shelf_life, purchase_price, selling_price):
        self.product_id = self.__class__.product_id
        self.__class__.product_id += 1
        self.category = category
        self.title = title
        self.unit = unit
        self.shelf_life = shelf_life
        self.purchase_price = purchase_price
        self.selling_price = selling_price

    def __repr__(self):
        return self.title
