# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:48:56 2015

Implementation of %METHOD_NAME% method, version %VERSION%
calculate.py
@author: Artem Sevastopolsky
"""

import time

# necessary params: A - matrix n x n, b - vector n x 1, eps - float

def calculate(params):
    '''Performs the main calculation procedure over the params.
    calculate(dict params) -> dict answer
    '''
    answer = {}
    answer['info'] = {'calcTime': None, 'iterNum': None}
    A, b, eps = answer['A'], answer['b'], answer['eps']
    startTime = time.time()
    iterNum = 0
    
    
    
    endTime = time.time()
    answer['info']['calcTime'] = endTime - startTime
    answer['info']['iterNum'] = iterNum
    return answer
