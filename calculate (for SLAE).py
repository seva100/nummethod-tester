# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:48:56 2015

calculate.py
@author: Artem Sevastopolsky
"""

# Here, finally, you can write the calculate function for your numMethod.
# Forget about testing. Just write a way to convert params to answer somehow.

import time
import numpy as np
import numpy.linalg as LA
#import scipy as sp

'''Necessary params: A - numpy matrix n x n,
                     b - numpy vector n x 1 (or 1 x n), 
                     eps - float, 
                     maxIter - int
'''

def calculate(params):
    '''Performs the main calculation procedure over the params.
    calculate(dict params) -> dict answer
    '''
    answer = {}
    A, b, eps, maxIter = answer['A'], answer['b'], answer['eps'], answer['maxIter']
    iterNum = 1
    startTime = time.time()
    
    pass
    
    endTime = time.time()
    answer['info'] = {'calcTime': endTime - startTime,
                    'iterNum': iterNum}
    return answer
