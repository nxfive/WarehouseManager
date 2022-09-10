from src.person.person import Person
from src.utils.utils import validation_input as validate
from src.warehouse.task import Task
import random


class Worker(Person):

    """Worker class is for workers w/o driver licence"""

    def __init__(self, warehouse, name, surname, age, experience):
        super().__init__(name, surname, age, experience)
        validate(name, 'name')
        validate(surname, 'surname')
        validate(age, 'age')
        self._name = name
        self._surname = surname
        self._age = age
        self._warehouse = warehouse
        self._experience = experience
        self._identity = id(self)
        self._change, self._job = self.get_change_and_job(warehouse)

    def __str__(self):
        return f'[{self.__class__.__name__}] Name: {self.name}, Surname: {self.surname}'

    def __repr__(self):
        return f"{self.__class__.__name__}=(name: '{self.name}', surname: '{self.surname}'"

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def identity(self):
        return self._identity

    @property
    def warehouse(self):
        return self._warehouse

    def get_change_and_job(self):
        structure = self.warehouse.warehouse_structure
        change = random.choice([key for key in structure.keys()])
        free_jobs = []
        for key, val in structure[change].items():
            for item in val:
                if item is None:
                    free_jobs.append(key)
                    break
        job = random.choice(free_jobs)
        for item in structure[change][job]:
            if item is None:
                structure[change][job][item] = self
                break
        return change, job
