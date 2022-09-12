import random
from src.warehouse.task import Task


class Product:
    """
        Product class describes products made from components on ProductProduction.
    """

    def __init__(self, name):
        self.name = name
        self.identity = id(self)
        self.needed_components = dict()
        # self.needed_time_for_one_pallet = random.randint(2, 10)    production??


class ProductProduction:
    # product: {component_index: amount_to_make_one, component_index: amount_to_make_one}
    # 10 products
    products_available = {'adart': {712653: 250, 789125: 25}, 'mustekt': {713355: 30, 725909: 350},
                          'opotez': {790422: 440, 790682: 50}, 'kofet': {764573: 100, 769438: 5},
                          'lomer': {712224: 555, 762785: 340}, 'detecta': {775328: 625, 789411: 10},
                          'juser': {787621: 940, 742821: 990}, 'dertus': {794665: 600, 777649: 820},
                          'zaks': {774963: 2, 740277: 32}, 'hamat': {771253: 322, 780346: 80, 797892: 1800}
                          }

    def __init__(self, warehouse, name):
        self.warehouse = warehouse
        self.name = name
        # self.cost_for_one_pallet = random.randint(500, 5000)
        self.stock = dict()
        self.products_components = {key: value for (key, value) in
                                    list(ProductProduction.products_available.items())[:1]}
        for item in self.products_components.keys():
            ProductProduction.products_available.pop(item)
        # if production is ready to make next product its True
        self.production_ready = True

    def _choose_product_and_amount(self):
        # 1. choose product
        choice_product = random.choice(list(self.products_components.keys()))
        print('choice_product', choice_product)
        # 2. choose how many we need to product
        how_many = random.randint(10, 25)
        self.production_ready = False
        return choice_product, how_many

    def _check_production_stock(self):
        choice_product, how_many = self._choose_product_and_amount()
        what_to_order = dict()  # stock - needed_components
        needed_components = {key: values * how_many for (key, values)
                             in self.products_components[choice_product].items()}
        print('needed_components', needed_components)
        for key, value in needed_components.items():
            if key in list(self.stock.keys()):
                what_to_order[key] = needed_components[key] - self.stock[key]
            else:
                what_to_order[key] = needed_components[key]
        return what_to_order

    def _check_warehouse_stock(self):
        what_to_order = self._check_production_stock()
        locations_with_needed_components = dict()  # {'A1_1': pallet_instance, 'A2_1':pallet_instance, ...}
        for key, value in self.warehouse.locations.items():
            if value is not None and value.index in (what_to_order.keys()):
                locations_with_needed_components[key] = value
        return locations_with_needed_components, what_to_order

    def _check_which_have_enough_quantity(self):
        locations_with_needed_components, what_to_order = self._check_warehouse_stock()
        print(locations_with_needed_components)
        print(what_to_order)
        # index : {quantity: [pallet_instance, ...]}}
        chosen = {}
        for index, quantity in what_to_order.items():
            for pallet in locations_with_needed_components.values():
                if index == pallet.index and index not in list(chosen.keys()):
                    chosen[index][quantity] = [pallet]
                elif index == pallet.index and index in list(chosen.keys()):
                    pallet = chosen[index][quantity].values()
                    if not pallet.quantity >= quantity:
                        chosen[index][quantity] += pallet
        return chosen

    def create_task(self):
        chosen_locations = self._check_which_have_enough_quantity()
        for quantity, values in chosen_locations.values():
            global amount
            amount = quantity
            for pallet in values:
                check_quantity = amount - pallet.quantity
                if check_quantity <= 0:
                    task = Task(pallet, pallet.index, amount, self.warehouse)
                    self.warehouse.tasks.append(task)
                else:
                    task = Task(pallet, pallet.index, pallet.amount, self.warehouse)
                    self.warehouse.tasks.append(task)
                    amount = check_quantity
