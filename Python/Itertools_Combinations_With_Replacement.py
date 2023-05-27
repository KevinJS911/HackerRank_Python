# -*- coding: utf-8 -*-
"""
Created on Sun May 28 00:18:58 2023

@author: kevin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string1, k = input().split()
k = int(k)
string2 = list(string1)
string2.sort()


comb = list(combinations_with_replacement(string2, k))
comb.sort()
for j in range(len(comb)):
    print (''.join(map(str, comb[j])))