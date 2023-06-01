# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:49:05 2023

@author: kevin
"""

import numpy

l = list(map(int, input().split()))

for i in range(len(l)):
    print (numpy.zeros((l[i], l[i]), dtype = numpy.int64), sep='\n \n')

for i in range(len(l)):
    print (numpy.ones((l[i], l[i]), dtype = numpy.int64), sep='\n \n')