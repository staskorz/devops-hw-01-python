from unittest import TestCase, main
from sys import argv
from datetime import datetime


# Assignment 3: Write a Python program that receives the Name of the user and his age,
#               then prints the Name and on which year he/she will reach the age of 120!
def willTurn120In(age):
    currentYear = datetime.today().year
    yearsTill120 = 120 - age
    return currentYear + yearsTill120


# Tests for assignment 3
class WillTurn120In(TestCase):
    def testHappyPath(self):
        self.assertEqual(willTurn120In(38), 2100)


# Run the test suite if invoked with "python -m unittest 3.py -v", otherwise run the prog
if __name__ == '__main__':
    if '--unittest' in argv: # run the unit test
        main()
    else: # run the program
        name = input('Please enter your name: ')
        age = int(input('Please enter your age: '))
        yearToTurn120 = willTurn120In(age)
        print(f'{name} will turn 120 in {yearToTurn120}')
