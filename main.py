# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:20:47 2015

Implementation of %METHOD_NAME% method, version %VERSION%
main.py
@author: Artem Sevastopolsky
"""

_method_name = None
_version = None

import os
from calculate import calculate
from TestFunc import (readTest, dumpTest, genTest, logStr)
from nmtester import NumMethodTester

curDirAbsPath = os.path.abspath(os.curdir)

tester = NumMethodTester()
# Fields that must be specified by instance owner
tester.TESTS_DIR = os.path.join(curDirAbsPath, "tests")
tester.TESTS_PAT = None
tester.PARAM_ORDER = (None, )
tester.TESTS_TO_CREATE_PROG = (None, )
tester.ANSWER_ORDER = (None, )
tester.LOG_DIR = os.path.join(curDirAbsPath, "logs")
tester.LOG_PAT = None
# Methods that must be specified by instance owner
tester.readTest = readTest
tester.dumpTest = dumpTest
tester.genTest = genTest
tester.calculate = calculate
tester.logStr = logStr

if __name__ == "__main__":
    tester.genAllTests()
    tester.makeFullLog()
    
    pass