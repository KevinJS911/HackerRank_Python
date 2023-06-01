# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:54:26 2023

@author: kevin
"""

import numpy

l = list(map(int, input().split()))
arr = numpy.array(l)
print (numpy.reshape(arr, (3,3)))