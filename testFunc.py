# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:20:45 2015

Implementation of Kachmazh method, version 1
testFunc.py
@author: Artem Sevastopolsky
"""

import os
#from pprint import pprint

TESTS_DIR = None
TESTS_PAT = None
TESTS_TO_CREATE_PROG = (None, )

def readTest(self, idx):
    '''Reads test from file "$self.TESTS_DIR/$self.TESTS_PAT".format(idx).
    Test should be stored in such way that the order of params doesn't matter.
    I/O Exceptions are not being caught.
    
    readTest(self, int idx) -> dict params
    '''
    fin = open(os.path.join(self.TESTS_DIR, self.TESTS_PAT.format(idx)))
    pass
    fin.close()

def dumpTest(self, idx, params):
    '''Stores test in file "$self.TESTS_DIR/$self.TESTS_PAT".format(idx).
    Test should be stored in such way that the order of params doesn't matter.
    I/O Exceptions are not being caught.
    
    dumpTest(self, int idx, dict params) -> None
    '''
    fout = open(os.path.join(self.TESTS_DIR, self.TESTS_PAT.format(idx)))
    pass
    fout.close()

def genTest(self, idx):
    '''Creates and dumps (using self.dumpTest) the test that should be
    created programmable way. Might support "pass" implementation if
    there's no such test. 
    
    If test with defined number already exist, it doesn't touch it.
    
    genTest(self, int idx) -> None
    '''
    pass

def logStr(self, answer):
    '''Makes string that is to be added to log file. It must show everything
    valuable from dict answer. May consist of multiple lines of text.
    
    logStr(self, dict answer) -> str logString
    '''
    ANSWER_ORDER = (None, )     # Specify this and then iterate by it
    logString = ""
    for el in ANSWER_ORDER:
        #if el == :
            pass
    return logString
