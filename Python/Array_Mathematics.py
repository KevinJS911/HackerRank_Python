# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:35:11 2023

@author: kevin
"""

import numpy as np

n,m = map(int, input().split())

row = []
for i in range(n):
    row.append(list(map(int, input().split())))

row1 = []
for j in range(n):
    row1.append(list(map(int, input().split())))

print (np.array(np.add(row, row1), int))
print (np.array(np.subtract(row, row1), int))
print (np.array(np.multiply(row, row1), int))
print (np.array(np.divide(row, row1), int))
print (np.array(np.mod(row, row1), int))
print (np.array(np.power(row, row1), int))