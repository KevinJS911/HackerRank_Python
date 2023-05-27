# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:34:54 2023

@author: kevin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

arr1 = list(map(int, input().split())) 
arr2 = list(map(int, input().split())) 

print (' '.join(map(str, product(arr1, arr2))))