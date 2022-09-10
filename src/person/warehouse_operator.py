from src.person.worker import Worker
from src.warehouse.task import Task
from src.warehouse.pallet import Pallet


class WarehouseOperator(Worker):

    def __init__(self, warehouse, name, surname, age, experience):
        super().__init__(warehouse, name, surname, age, experience)
        self.added_tasks = []
        self.tasks_done = []

    def show_added_tasks(self):
        for task in self.added_tasks:
            print(task)

    def do_the_task(self):
        for task in self.added_tasks:
            if self.warehouse.locations[task.to_location] is None:
                self.warehouse.locations[task.to_location] = Pallet(task.to_location, task.handling_unit_number,
                                                                    task.index_number, task.quantity)
            else:
                print("This location is full. Change location manually.")
                print("List of empty location:\n")
                empty_locations = []
                for location, value in self.warehouse.locations.items():
                    if value is None:
                        empty_locations.append(location)
                        print(location)
                new_location = input('Enter new location: ')
                while new_location not in empty_locations:
                    new_location = input('Enter new location: ').upper()
                self.warehouse.locations[new_location] = Pallet(task.to_location, task.handling_unit_number,
                                                                task.index_number, task.quantity)

    def unload_delivery(self, warehouse):
        if self._job == 'Receipt':
            for ramp in warehouse.busy_ramps:
                if ramp is not None:
                    for identity, quantity in ramp.delivery_note.items():
                        task = Task('Ground Zone', identity, quantity, warehouse)
                        Task.tasks.append(task)
                        self.tasks_done.append(task)  # done for worker on receipt of goods
                    break
        else:
            print('Its NOT my job!')
