# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:48:39 2023

@author: kevin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
arr = list(input().split())
l = tuple(map(int, arr))
print (hash(l))