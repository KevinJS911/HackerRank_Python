# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:51:46 2023

@author: kevin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string1, k = input().split()
k = int(k)
string2 = list(string1)
string2.sort()

for i in range(int(k)):
    comb = list(combinations(string2, i+1))
    comb.sort()
    for j in range(len(comb)):
        print (''.join(map(str, comb[j])))