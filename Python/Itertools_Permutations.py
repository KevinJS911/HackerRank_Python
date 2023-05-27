# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:41:28 2023

@author: kevin
"""

from itertools import permutations

string, k = input().split()
p = list(permutations(string, int(k)))
p.sort()

for i in range(len(p)):
    print (''.join(map(str, p[i])))