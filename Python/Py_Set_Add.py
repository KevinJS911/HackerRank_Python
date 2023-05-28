# -*- coding: utf-8 -*-
"""
Created on Sun May 28 13:59:28 2023

@author: kevin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

arr = []
for i in range(n):
    arr.append(str(input()))
    
print (len(set(arr)))