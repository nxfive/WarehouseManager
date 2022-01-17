import random
from task import Task
from warehouse import Warehouse


class Product:
    # products ready to location
    products = []
    tasks = []

    def __init__(self):
        self._location = 'Ground zone'
        self._index_number = Product.get_index_number()
        self._quantity = Product.get_quantity()

    def __str__(self):
        return f'Index number: {self.index_number}, Quantity: {self.quantity}'

    @property
    def location(self):
        return self._location

    @property
    def index_number(self):
        return self._index_number

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @staticmethod
    def get_index_number():
        indexes_of_products = [
            712653, 789125, 713355, 725909, 790422, 790682, 764573,
            769438, 712224, 762785, 775328, 789411, 787621, 742821,
            794665, 777649, 774963, 740277, 771253, 780346, 781628,
            797892, 735685, 773965, 754382, 753231, 712272, 766161,
            727250, 729939, 786515, 735443, 747347, 753239, 715864,
            713945, 714839, 789851, 769109, 733279, 797409, 733538,
            714979, 732648, 731372, 781936, 768242, 753357, 796413
        ]
        choice_index = random.choice(indexes_of_products)
        return choice_index

    @staticmethod
    def get_quantity():
        quantity_of_products = [1200, 480, 860, 11200, 120,
                                4500, 2850, 320, 500, 1360,
                                300, 790, 925, 1000, 3200]
        choice_quantity = random.choice(quantity_of_products)
        return choice_quantity

    @classmethod
    def add_product_to_products(cls, product):
        Product.products.append(product)
