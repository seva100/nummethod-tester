# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:20:45 2015

mytester.py
@author: Artem Sevastopolsky
"""

# Here you should implement class inherited from NumMethodTester - MyTester.
# To implement it, write implementations of methods with "pass" statements inside:
#   readTest
#   dumpTest (in case you want to make some tests by program)
#   genTest (in case you want to make some tests by program - uses dumpTest)
#   logStr (in case you want to have a report)
#

import os
#from pprint import pformat
from nmtester import NumMethodTester
from calculate import calculate

class MyTester(NumMethodTester):
    
    def __init__(self):
        self.curDirAbsPath = os.path.abspath(os.curdir)
        self.TESTS_DIR = os.path.join(self.curDirAbsPath, "tests")
        self.TESTS_PAT = "test {}"
        self.TESTS_TO_CREATE_PROG = (4, 5, 6, )
        self.LOG_DIR = os.path.join(self.curDirAbsPath, "logs")
        self.LOG_PAT = "log {}"
        self.calculate = calculate
    
    def readTest(self, testNo):
        '''Reads test from file "$self.TESTS_DIR/$self.TESTS_PAT".format(testNo).
        It's useful when test is stored in such way that the order of params 
        doesn't matter and can be recognized.
        I/O Exceptions are not being caught.
        
        readTest(self, int testNo) -> dict params
        '''
        
        fin = open(os.path.join(self.TESTS_DIR, self.TESTS_PAT.format(testNo)))
        params = {}
        pass
        fin.close()
        return params
    
    def dumpTest(self, testNo, params):
        '''Stores test in file "$self.TESTS_DIR/$self.TESTS_PAT".format(testNo).
        Test should be stored in such way that the order of params
        doesn't matter and can be recognized.
        I/O Exceptions are not being caught.
        
        dumpTest(self, int testNo, dict params) -> None
        '''
        fout = open(os.path.join(self.TESTS_DIR, self.TESTS_PAT.format(testNo)), 'w')
        pass
        fout.close()
    
    def genTest(self, testNo):
        '''Creates and dumps (using self.dumpTest) the test that should be
        created programmable way. Might support "pass" implementation if
        there's no such test. 
        
        If test with defined number already exist, it doesn't touch it.
        
        genTest(self, int testNo) -> None
        '''
        params = {}
        #if testNo == :
            pass
        #elif testNo == :
        self.dumpTest(params)
    
    def logStr(self, answer):
        '''Makes string that is to be added to log file. It must show everything
        valuable from dict answer. May consist of multiple lines of text.
        
        logStr(self, dict answer) -> str logString
        '''
        ANSWER_ORDER = (None, )     # You can specify this and then iterate by it
        logString = ""
        for el in ANSWER_ORDER:
            #if el == :
                pass
        return logString
