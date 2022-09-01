import random


class Component:
    # products ready to location
    components = []
    indexes_quantity_available = {
        712653: 1720, 789125: 250, 713355: 390, 725909: 1200, 790422: 1430, 790682: 590, 764573: 1000,
        769438: 780, 712224: 6000, 762785: 4500, 775328: 1245, 789411: 120, 787621: 1587, 742821: 4210,
        794665: 1100, 777649: 2600, 774963: 100, 740277: 470, 771253: 2560, 780346: 1030, 797892: 8640}
    # quantity should be chosen by company??

    # 781628, 735685, 773965, 754382, 753231, 712272, 766161,
    # 727250, 729939, 786515, 735443, 747347, 753239, 715864,
    # 713945, 714839, 789851, 769109, 733279, 797409, 733538,
    # 714979, 732648, 731372, 781936, 768242, 753357, 796413}

    def __init__(self):
        self._location = 'Ground zone'
        try:
            indexes = [index for index in Component.indexes_quantity_available.keys()]
            self._index_number = random.choice(indexes)
        except ValueError:
            print('There is no more available indexes.')
        self._quantity = int(''.join([value for (key, value) in Component.indexes_quantity_available.items()
                             if key == self._index_number]))
        Component.components.append(self)
        Component.indexes_quantity_available.pop(self._index_number)

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
