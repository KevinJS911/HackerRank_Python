# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:28:32 2023

@author: kevin

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
"""

import numpy as np
n, m, p = map(int, input().split())

row = []
for i in range(n):
    row.append(list(map(int, input().split())))

row1 = []
for i in range(m):
    row1.append(list(map(int, input().split())))

print (np.concatenate((np.array(row), np.array(row1))))
