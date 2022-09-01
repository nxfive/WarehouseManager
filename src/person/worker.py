from src.person.person import Person
from src.utils import validation_input as validate
from src.warehouse.task import Task


class Worker(Person):

    """Worker class is for workers w/o driver licence"""

    def __init__(self, name, surname, age, experience):
        validate(name, 'name')
        validate(surname, 'surname')
        validate(age, 'age')
        self._name = name
        self._surname = surname
        self._age = age
        self._experience = experience
        self._identity = id(self)
        self.tasks = Task.tasks

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
