import random


class Product:
    """
        Product class describes products made from components on ProductProduction.
    """

    def __init__(self, name):
        self.name = name
        self.identity = id(self)
        self.needed_components = dict()
        self.needed_time_for_one_pallet = random.randint(2, 10)


class ProductProduction:

    # 10 products
    products_available = ['anti-noise headphones', 'helmets', '']

    def __init__(self, name, identity, amount):
        self.name = name
        self.cost_for_one_pallet = random.randint(500, 5000)
