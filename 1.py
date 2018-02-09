from unittest import TestCase, main
from functools import reduce


# Assignment 1.A: Write a Python function that calculates the Sum of the list
def sum(lst):
	lstLen = len(lst)
	if lstLen == 0:
		return 0

	return reduce((lambda a, b: a + b), lst)


# Assignment 1.B: Write a Python function that calculates the Average of the list
def avg(lst):
	lstLen = len(lst)
	if lstLen == 0:
		return 0
	
	lstSum = sum(lst)
	return lstSum / lstLen


# Test subject
testList = [4, 2 , 7 , 8, 9, 10, 2, 8, 6]


# Tests for assignment 1.A
class SumTest(TestCase):
	def testHappyPath(self):
		self.assertEqual(sum(testList), 56)
	
	def testEmptyList(self):
		self.assertEqual(sum([]), 0)
	
	def testSingleElementList(self):
		self.assertEqual(sum([5]), 5)


# Tests for assignment 1.B
class AvgTest(TestCase):
	def testHappyPath(self):
		self.assertEqual(round(avg(testList), 5), 6.22222)
	
	def testEmptyList(self):
		self.assertEqual(avg([]), 0)
	
	def testSingleElementList(self):
		self.assertEqual(avg([5]), 5)


# Run the test suite
if __name__ == '__main__':
    main()
