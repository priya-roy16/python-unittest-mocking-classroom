from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDb(TestCase):
	@patch('src.db_helper.DbHelper')
	def test_max_salary_is_greater_than_min_salary(self, MockDb):
		db_helper = MockDb()

		db_helper.get_maximum_salary.return_value = 10
		db_helper.get_minimum_salary.return_value = 1

		maximum_salary = db_helper.get_maximum_salary()
		minimum_salary = db_helper.get_minimum_salary()

		self.assertGreater(maximum_salary, minimum_salary)