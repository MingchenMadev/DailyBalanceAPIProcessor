from DailyBalanceAPIProcessor import *
from decimal import *
import unittest

class DailyBalanceAPIProcessorTest(unittest.TestCase):
	def setUp(self):
		self.dbAPIprocessor = DailyBalanceAPIProcessor()

	def test_read_from_url_negative(self):
		"""
	    Negative test for DailyBalanceAPIProcessor for url of status code not 200.

	    """
		for i in range(5, 10):
			url = 'https://resttest.bench.co/transactions/' + str(i) + '.json'
			self.assertFalse(self.dbAPIprocessor.read_from_url(url))

	def test_dailyBalance_content(self):
		"""
	    Positivee test for DailyBalanceAPIProcessor for urls of status code 200.
	    Testing the data correctness, to see if the balance calculation is correct.

	    """

		for i in range(1, 4):
			url = 'https://resttest.bench.co/transactions/' + str(i) + '.json'
			self.assertTrue(self.dbAPIprocessor.read_from_url(url))
		self.assertEqual(self.dbAPIprocessor.dateToBalance['2013-12-22'], Decimal('-110.71'))
		self.assertEqual(self.dbAPIprocessor.dateToBalance['2013-12-21'], Decimal('-17.98'))

if __name__ == "__main__":
	unittest.main()