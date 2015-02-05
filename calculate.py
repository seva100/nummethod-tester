# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:48:56 2015

calculate.py
@author: Artem Sevastopolsky
"""

# Here, finally, you can write the calculate function for your numMethod.
# Forget about testing. Just write a way to convert params to answer somehow.

import time
#import numpy as np
#import numpy.linalg as LA
#import scipy as sp

def calculate(params):
    '''Performs the main calculation procedure over the params.
    calculate(dict params) -> dict answer
    '''
    # You can print a debug info onto the main screen
    
    answer = {}
    iterNum = 1
    startTime = time.time()
    pass        # Write the code here
    endTime = time.time()
    answer['info'] = {'calcTime': endTime - startTime,
                    'iterNum': iterNum}
    return answer