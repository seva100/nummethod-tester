# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:20:47 2015

main.py
@author: Artem Sevastopolsky
"""

# This is the script you're going to run.
# You can specify _method_name and _version for convenience.

_method_name = None
_version = None

from myTester import MyTester

tester = MyTester()

if __name__ == "__main__":
    tester.checkAssigned()
    # You can call genTests.genAllTests(tester) here, or do it only once
    tester.makeFullLog()    # you can comment this if you don't want to make a report.
    
    # Here you can add some testing functionality: plot graphs of solutions,
    # make comparisons or etc. In order to do that, you can use 
    #   answer = tester.getAnswerFor(testNo)
    # and do smth with this answer.
    
    pass