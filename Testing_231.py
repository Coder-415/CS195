#Use unittest.TestCase methods to confirm that the addition and subtraction of date and timedelta objects produce correct results 

#importing modules 
import datetime
from datetime import timedelta
import unittest


#classes and methods to demonstrate unittest and verify ability to add and subtract dates uisng timedelta
class dates():
	def add_date(x):
		return datetime.date(2020,10,11) + timedelta (days = x)
	def subtract_date(y):
		return datetime.date(2020,10,11) - timedelta (days = y)


class TestTimeMethods(unittest.TestCase):

#testing using both .assertEqual to test valid output and .assertRaises to test type error if string entered  

	def test_addition_of_date(self):
		Halloween = datetime.date(2020,10,31)
		self.assertEqual(dates.add_date(20),Halloween)
		with self.assertRaises (TypeError):
			dates.add_date('twenty')

#testing using .assertNotEqual while changing only the year, .assertAlmostEqual while ensuring will round down, 
#and .assertRaises will failing to enter a value leading to a TypeError 

	def test_subtraction_of_date(self):
		self.assertNotEqual(dates.subtract_date(10),datetime.date(2019,10,1))
		self.assertAlmostEqual (dates.subtract_date(0.001),datetime.date(2020,10,11),places=2)
		with self.assertRaises (TypeError):
			dates.add_date()

unittest.main()
