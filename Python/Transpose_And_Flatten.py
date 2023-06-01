# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:55:22 2023

@author: kevin
"""

import numpy as np

n, m = input().split()
n = int(n)
m = int(m)

row = []
for i in range(n):
    row.append(list(map(int, input().split())))

row = np.reshape(row, (n,m))

print (row.transpose())
print (row.flatten())
