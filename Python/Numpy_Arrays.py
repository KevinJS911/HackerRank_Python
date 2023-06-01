# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:06:53 2023

@author: kevin
"""

import numpy

def arrays(arr):
    arr.reverse()
    return (numpy.array(arr, float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)