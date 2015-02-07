# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 12:43:22 2015

genTests.py
@author: Artem Sevastopolsky
"""

from ./mytester import MyTester

def genTest(tester, testNo):
    tester.genTest(testNo)

def genAllTests(tester):
    tester.genAllTests()

if __name__ == '__main__':
    tester = MyTester()
    genAllTests(tester)
