# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:37:31 2015

NumMethodTester lib (nmtester).
Build to help testing Numerical Methods.
nmtester.py

@author: Artem Sevastopolsky
"""

import os
import re
from datetime import datetime

class NumMethodTester:
    
    # Fields that must be specified by instance owner
    TESTS_DIR = None
    TESTS_PAT = None
    TESTS_TO_CREATE_PROG = (None, )
    LOG_DIR = None
    LOG_PAT = None
    
    # Methods that must be specified by instance owner
    readTest = None
    dumpTest = None
    genTest = None
    logStr = None
    calculate = None
    
    def checkAssigned(self):
        '''Checks that all fields and methods of the class have been overloaded
        (or assigned) by instance owner.'''
        assert self.TESTS_DIR
        assert self.TESTS_PAT
        assert self.TESTS_TO_CREATE_PROG
        assert self.LOG_DIR
        assert self.LOG_PAT
        
        assert self.readTest
        assert self.dumpTest
        assert self.genTest
        assert self.logStr
        assert self.calculate
    
    def genAllTests(self):
        '''Creates and dumps (using self.genTest) all tests that should be 
        created programmable way. The sequence of those tests should be set
        as the self.TESTS_TO_CREATE_PROG tuple by hand.
        
        self.genAllTests() -> None
        '''
        for testNo in self.TESTS_TO_CREATE_PROG:
            self.genTest(testNo)
    
    def listAllTests(self):
        '''Shows numbers of all tests in folder self.TESTS_DIR that respond to
        pattern self.TESTS_PAT.
        I/O exceptions are not being caught.
        
        self.listAllTests() -> tuple testNumbers
        '''
        allFileNames = os.listdir(self.TESTS_DIR)
        reTestPat = '^' + self.TESTS_PAT.replace('{}', r'(\d*)') + '$'
        testsNo = []
        for el in allFileNames:
            lst = re.findall(reTestPat, el)
            if lst:
                testsNo.append(int(lst[0]))
        testsNo.sort()
        return tuple(testsNo)
    
    def getAnswerFor(self, testNo):
        '''Reads a desired test and returns the answer to it.
        
        self.getAnswerFor(testNo) -> dict answer
        '''
        inputParams = self.readTest(testNo)
        answer = self.calculate(inputParams)
        return answer
    
    def getLastLogNo(self):
        '''Returns the greatest number of log existing in self.LOG_DIR that 
        responds to self.LOG_PAT.
        I/O exceptions are not being caught.
        '''
        allFileNames = os.listdir(self.LOG_DIR)
        reLogPat = '^' + self.LOG_PAT.replace('{}', r'(\d*)') + '$'
        logsNo = []
        for el in allFileNames:
            lst = re.findall(reLogPat, el)
            if lst:
                logsNo.append(int(lst[0]))
        if len(logsNo) == 0:
            return 0
        else:
            return max(logsNo)
    
    def _makeLogWithContent(self, stringToWrite):
        '''Makes new log in self.LOG_DIR according to self.LOG_PAT 
        with content stringToWrite. 
        No. of new log will be the greatest existing + 1.'''
        logFN = self.LOG_PAT.format(self.getLastLogNo() + 1)
        
        fout = open(os.path.join(self.LOG_DIR, logFN), 'w')
        fout.write(stringToWrite)
        
        fout.close()
        
    def makeLogForTest(self, testNo):
        '''Makes new log in self.LOG_DIR according to self.LOG_PAT 
        for test testNo. No. of new log will be the greatest existing + 1.'''
        inputParams = self.readTest(testNo)
        outputParams = self.calculate(inputParams)
        
        stringToWrite = 'Created on ' + str(datetime.now()) + '\n' + \
                        '=' * 30 + ' TEST #{} '.format(testNo) + '=' * 30 + '\n' \
                        + self.logStr(outputParams)
        self._makeLogWithContent(stringToWrite)
        
    
    def makeFullLog(self):
        '''Makes new log in self.LOG_DIR according to self.LOG_PAT 
        for all tests in self.TEST_DIR. 
        No. of new log will be the greatest existing + 1.'''
        stringToWrite = 'Created on ' + str(datetime.now()) + '\n'
        for testNo in self.listAllTests():
            inputParams = self.readTest(testNo)
            outputParams = self.calculate(inputParams)
            stringToWrite += '=' * 30 + ' TEST #{} '.format(testNo) + '=' * 30 + '\n' \
                + self.logStr(outputParams)
        self._makeLogWithContent(stringToWrite)
    
    