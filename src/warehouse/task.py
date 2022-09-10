import random


class Task:

    tasks = []

    def __init__(self, from_location, identity, quantity, warehouse):
        self.from_location = from_location
        self.handling_unit_number = int(str(400125) + str(random.randint(100000, 999999)))
        self.index_number = identity
        self.quantity = quantity
        self.to_location = Task.get_to_location(warehouse)

# TODO: Task methods:
# show details of task
# who done this task
# check time of last update
# check location
# check all history of the task

    def __str__(self):
        return f'From location: {self.from_location}\nHandling unit: {self.handling_unit_number}\n' \
               f'Index: {self.index_number}\nQuantity: {self.quantity}\nTo location: {self.to_location}\n' \
               f'--------------------------------'

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
        for task in Task.tasks:
            print(task)

    def check_location(self):
        return self.from_location
