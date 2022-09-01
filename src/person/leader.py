from src.person.worker import Worker


class Leader(Worker):

    def __init__(self, name, surname, age, experience):
        super().__init__(name, surname, age, experience)

    def create_an_order(self):
        pass
