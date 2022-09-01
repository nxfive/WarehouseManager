from src.person.worker import Worker


class WarehouseOperator(Worker):

    _instances = 11

    def __init__(self, name, surname, age, experience):
        super().__init__(name, surname, age, experience)
        try:
            self._change = WarehouseOperator.get_change()
        except IndexError:
            raise IndexError('Too many workers')
        self._job = get_job(self)
        if self._job == 'Placement' or self._job == 'Release':
            self.added_tasks = []
            self.tasks_done = []

    @property
    def job(self):
        return self._job

    @property
    def change(self):
        return self._change

    def get_job(self):
        dict_jobs = self._warehouse_structure[self.change]
        free = []
        for key, val in dict_jobs.items():
            for v in val:
                if v is None:
                    free.append(key)
                    break
        job = choice(free)
        return

    @staticmethod
    def get_job_1():
        if WarehouseOperator.jobs:
            choice_job = choice(WarehouseOperator.jobs)
            WarehouseOperator.jobs.remove(choice_job)
            return choice_job
        else:
            return 'Release'

    @staticmethod
    def get_change():
        if WarehouseOperator.change_A != 10:
            return 'change A'
        elif WarehouseOperator.change_B != 10:
            return 'change B'
        elif WarehouseOperator.change_C != 10:
            return 'change C'

    @classmethod
    def add_to_change(cls, worker):
        if worker.change == 'change A':
            WarehouseOperator.change_A.append(worker)
        if worker.change == 'change B':
            WarehouseOperator.change_B.append(worker)
        if worker.change == 'change C':
            WarehouseOperator.change_C.append(worker)

    @classmethod
    def add_to_job_group(cls, worker):
        if worker.job == 'Release':
            WarehouseOperator.release.append(worker)
        if worker.job == 'Shipping':
            WarehouseOperator.shipping.append(worker)
        if worker.job == 'Placement':
            WarehouseOperator.placement.append(worker)
        if worker.job == 'Receipt':
            WarehouseOperator.receipt.append(worker)

    @staticmethod
    def show_added_tasks_to_workers():
        for person in WarehouseOperator.placement:
            if person.added_tasks:
                print(person.added_tasks)

    def add_tasks(self):
        if Task.new_tasks:
            for task in Task.new_tasks:
                self.added_tasks.append(task)
                Task.new_tasks.remove(task)

    def do_the_task(self):
        for task in self.added_tasks:
            if Warehouse.locations[task.to_location] is None:
                Warehouse.locations[task.to_location] = task.handling_unit_number
            else:
                print("This location is full. Change location manually.")
                print("List of empty location:\n")
                empty_locations = []
                for location, value in Warehouse.locations.items():
                    if value is None:
                        empty_locations.append(location)
                        print(location)
                new_location = input('Enter new location: ')
                while new_location not in empty_locations:
                    new_location = input('Enter new location: ').upper()
                Warehouse.locations[new_location] = task.handling_unit_number




    @property
    def instances(self):
        return self._instances
