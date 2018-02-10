from unittest import TestCase, main
from functools import reduce


# Assignment 1: Write a Python function that counts the vowels (a, e, i, o, u) in a given string
def countVowels(string):
    vowels = 'aeiou'

    return reduce(lambda count, char: count + 1 if char in vowels else count, string, 0)


# Test subject
testString = "example"


# Tests for assignment 1
class CountVowelsTest(TestCase):
    def testHappyPath(self):
        self.assertEqual(countVowels(testString), 3)


# Run the test suite
if __name__ == '__main__':
    main()
