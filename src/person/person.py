from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def __init__(self, name, surname, age, experience):
        self.name = name
        self.surname = surname
        self.age = age
        self.experience = experience

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
