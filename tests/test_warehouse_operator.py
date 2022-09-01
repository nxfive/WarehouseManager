import unittest
from src.person.warehouse_operator import WarehouseOperator
from unittest.mock import patch


def setUpModule():
    print('setting up module')
    global wop
    wop = WarehouseOperator('Name', 'Surname', 20)


def tearDownModule():
    print('tearing down module...')
    global wop
    del wop


class TestGetJob(unittest.TestCase):

    @patch.object(WarehouseOperator, 'get_job')
    def test_get_job_when_jobs_list_is_full(self, mocked_method):
        mocked_method.return_value = 'Placement'
        actual = wop.get_job()
        expected = 'Placement'
        self.assertEqual(actual, expected)

    def test_get_job_when_jobs_list_is_empty(self):
        wop.jobs.clear()
        self.assertEqual(wop.get_job(), 'Release')


class TestGetChange(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()