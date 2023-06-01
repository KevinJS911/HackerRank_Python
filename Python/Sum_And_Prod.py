# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:48:19 2023

@author: kevin
"""

import numpy as np
n,m = map(int, input().split())

row = []
for i in range(n):
    row.append(list(map(int, input().split())))

print (np.product(np.sum(row, axis=0)))
    



