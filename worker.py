import random
from task import Task
from warehouse import Warehouse


class Worker:

    def __init__(self, name: str, surname: str, age: int):
        Worker.validation_input(name, 'name')
        Worker.validation_input(surname, 'surname')
        Worker.validation_input(age, 'age')
        self._name = name
        self._surname = surname
        self._age = age
        self._identity = Worker.get_identity()

    def __str__(self):
        return f'Name: {self.name} Surname: {self.surname}'

    def __repr__(self):
        return f'{self.__class__.__name__.capitalize()}=({self.name, self.surname, self.age}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Worker.validation_value(self, value, 'name')

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        Worker.validation_value(self, value, 'surname')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        Worker.validation_value(self, value, 'age')

    @property
    def identity(self):
        return self._identity

    @staticmethod
    def get_identity():
        first_ide = ''
        for _ in range(3):
            first_ide += random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
                                        's', 't', 'u', 'w', 'x', 'y', 'z']).upper()
        sec_ide = random.randint(123456, 234567)
        return first_ide + str(sec_ide)

    @staticmethod
    def validation_input(value, value_name):
        if value_name == 'name' or value_name == 'surname':
            if not isinstance(value, str):
                raise TypeError(f'{value_name.capitalize()} value must be str not {type(value).__name__}.')
            if not value.isalpha():
                raise ValueError(f'{value_name.capitalize()} should only include alphabetic object.')
        if value_name == 'age':
            if isinstance(value, str):
                try:
                    int(value)
                except ValueError:
                    print('Cannot change value str to int.')
            if not isinstance(value, (str, int)):
                raise TypeError(f'Age value cannot be other than str if its a num or int.')

    def validation_value(self, value, value_name: str):
        if value_name == 'name' or value_name == 'surname':
            if not isinstance(value, str):
                raise TypeError(f'{value_name.capitalize()} value cannot be other than str.')
            if not value.isalpha():
                raise ValueError(f'{value_name.capitalize()} value must be alphabetic.')
            return self.name if 'name' else self.surname

        if value_name == 'age':
            if isinstance(value, str):
                try:
                    int(value)
                except ValueError:
                    print('Cannot change str to int.')
            if not isinstance(value, (str, int)):
                raise TypeError(f'{value_name.capitalize()} can only be type str if its number or int.')
            return self._age


class WarehouseOperator(Worker):

    _amount_of_workers_at_change = 11
    jobs = ['Shipping', 'Shipping',
            'Receipt', 'Receipt',
            'Placement', 'Placement']

    shipping = []
    receipt = []
    placement = []
    release = []

    change_A = []
    change_B = []
    change_C = []

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self._job = WarehouseOperator.get_job()
        if self._job == 'Placement' or self._job == 'Release':
            self.added_tasks = []
            self.tasks_done = []
        try:
            self._change = WarehouseOperator.get_change()
        except IndexError:
            print('Too many workers')

    @property
    def job(self):
        return self._job

    @property
    def change(self):
        return self._change

    @staticmethod
    def get_job():
        if WarehouseOperator.jobs:
            choice_job = random.choice(WarehouseOperator.jobs)
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
        if worker.job == 'Release':
            WarehouseOperator.release.append(worker)

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
