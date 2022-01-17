import random


class Task:

    new_tasks = []

    def __init__(self, from_location, product, warehouse):
        self.from_location = from_location
        self.handling_unit_number = Task.get_handling_unit_number()
        self.index_number = product.index_number
        self.quantity = product.quantity
        self.to_location = Task.get_to_location(warehouse)

    def __str__(self):
        return f'From location: {self.from_location}\nHandling unit: {self.handling_unit_number}\n' \
               f'Index: {self.index_number}\nQuantity: {self.quantity}\nTo location: {self.to_location}'

    @staticmethod
    def get_handling_unit_number():
        handling_unit = str(400125) + str(random.randint(100000, 999999))
        return int(handling_unit)

    @staticmethod
    def get_to_location(warehouse):
        empty_locations = []
        for key, val in warehouse.locations.items():
            if val is None:
                empty_locations.append(key)

        choice_location = random.choice(empty_locations)
        return choice_location

    @classmethod
    def display_tasks(cls):
        for task in Task.new_tasks:
            print(task)
