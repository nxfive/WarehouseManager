from src.person.worker import Worker
import unittest
from parameterized import parameterized

test_parameters = [
    ('int_value', 12345),
    ('float_value', 12.5),
    ('int_value_in_single_quotes', '12345'),
    ('float_value_in_single_quotes', '12.5'),
    ('string_with_number_value_in_single_quotes', 'ABC12'),
    ('string_with_other_value_in_single_quotes', 'ABC#'),
]


class TestWorkerInputValidation(unittest.TestCase):

    @parameterized.expand(test_parameters)
    def test_invalid_name_value_should_raise_error(self, test_name, name):
        if isinstance(name, (int, float)):
            self.assertRaises(TypeError, Worker, name, 'Surname', 20)
        else:
            self.assertRaises(ValueError, Worker, name, 'Surname', 20)

    @parameterized.expand(test_parameters)
    def test_invalid_surname_value_should_raise_error(self, test_name, surname):
        if isinstance(surname, (int, float)):
            self.assertRaises(TypeError, Worker, 'Name', surname, 20)
        else:
            self.assertRaises(ValueError, Worker, 'Name', surname, 20)

    @parameterized.expand([
        ('float_value', 12.5, TypeError),
        ('float_value_in_single_quotes', '12.5', ValueError),
        ('other_value_in_single_quotes', '@%$%', ValueError),

    ])
    def test_invalid_age_value_should_raise_error(self, test_name, age, error):
        with self.assertRaises(error):
            Worker('Name', 'Surname', age)


class TestWorkerValueValidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up class...')
        cls.worker = Worker('Name', 'Surname', 20)

    @parameterized.expand(test_parameters)
    def test_invalid_name_value_should_raise_error(self, test_name, name):
        if isinstance(name, (int, float)):
            with self.assertRaises(TypeError):
                self.worker.name = name
        else:
            with self.assertRaises(ValueError):
                self.worker.name = name

    @parameterized.expand(test_parameters)
    def test_invalid_surname_value_should_raise_error(self, test_name, surname):
        if isinstance(surname, (int, float)):
            with self.assertRaises(TypeError):
                self.worker.surname = surname
        else:
            with self.assertRaises(ValueError):
                self.worker.surname = surname

    @parameterized.expand([
        ('float_value', 12.5, TypeError),
        ('float_value_in_single_quotes', '12.5', ValueError),
        ('other_value_in_single_quotes', '@%$%', ValueError),

    ])
    def test_invalid_age_value_should_raise_error(self, test_name, age, error):
        with self.assertRaises(error):
            self.worker.age = age


if __name__ == '__main__':
    unittest.main(verbosity=2)
