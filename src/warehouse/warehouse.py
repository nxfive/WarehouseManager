from src.person.warehouse_operator import WarehouseOperator


class Warehouse:

    _change_structure = {'shipping': WarehouseOperator._instances,
                         'receipt': WarehouseOperator._instances,
                         'placement': WarehouseOperator._instances,
                         'release': WarehouseOperator._instances}

    _warehouse_structure = {'change_A': _change_structure,
                            'change_B': _change_structure,
                            'change_C': _change_structure}

    # amount of people per change
    _changes = {change: len(WarehouseOperator._instances) for change in _warehouse_structure.keys()}

    def __init__(self, name):
        self._name = name
        self._tasks = []
        self._capacity = 144
        self._ramps = 4
        self._locations = {
            'A1_1': None, 'A1_2': None, 'A1_3': None,
            'A2_1': None, 'A2_2': None, 'A2_3': None,
            'A3_1': None, 'A3_2': None, 'A3_3': None,
            'A4_1': None, 'A4_2': None, 'A4_3': None,
            'A5_1': None, 'A5_2': None, 'A5_3': None,
            'A6_1': None, 'A6_2': None, 'A6_3': None,
            'A7_1': None, 'A7_2': None, 'A7_3': None,
            'A8_1': None, 'A8_2': None, 'A8_3': None,
            'A9_1': None, 'A9_2': None, 'A9_3': None,
            'A10_1': None, 'A10_2': None, 'A10_3': None,
            'B1_1': None, 'B1_2': None, 'B1_3': None,
            'B2_1': None, 'B2_2': None, 'B2_3': None,
            'B3_1': None, 'B3_2': None, 'B3_3': None,
            'B4_1': None, 'B4_2': None, 'B4_3': None,
            'B5_1': None, 'B5_2': None, 'B5_3': None,
            'B6_1': None, 'B6_2': None, 'B6_3': None,
            'B7_1': None, 'B7_2': None, 'B7_3': None,
            'B8_1': None, 'B8_2': None, 'B8_3': None,
            'B9_1': None, 'B9_2': None, 'B9_3': None,
            'B10_1': None, 'B10_2': None, 'B10_3': None,
            'C1_1': None, 'C1_2': None, 'C1_3': None,
            'C2_1': None, 'C2_2': None, 'C2_3': None,
            'C3_1': None, 'C3_2': None, 'C3_3': None,
            'C4_1': None, 'C4_2': None, 'C4_3': None,
            'C5_1': None, 'C5_2': None, 'C5_3': None,
            'C6_1': None, 'C6_2': None, 'C6_3': None,
            'C7_1': None, 'C7_2': None, 'C7_3': None,
            'C8_1': None, 'C8_2': None, 'C8_3': None,
            'C9_1': None, 'C9_2': None, 'C9_3': None,
            'C10_1': None, 'C10_2': None, 'C10_3': None,
            'D1_1': None, 'D1_2': None, 'D1_3': None,
            'D2_1': None, 'D2_2': None, 'D2_3': None,
            'D3_1': None, 'D3_2': None, 'D3_3': None,
            'D4_1': None, 'D4_2': None, 'D4_3': None,
            'D5_1': None, 'D5_2': None, 'D5_3': None,
            'D6_1': None, 'D6_2': None, 'D6_3': None,
            'D7_1': None, 'D7_2': None, 'D7_3': None,
            'D8_1': None, 'D8_2': None, 'D8_3': None,
            'D9_1': None, 'D9_2': None, 'D9_3': None,
            'D10_1': None, 'D10_2': None, 'D10_3': None}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @property
    def ramps(self):
        return self._ramps

    def check_location(self, location):
        print(self._locations[location])

    def show_empty_locations(self):
        for key, value in self._locations.items():
            if value is None:
                print(key, value)

    def show_nonempty_locations(self):
        for key, value in self._locations.items():
            if value is not None:
                print(key, value)
