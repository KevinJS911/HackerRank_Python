# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:27:11 2023

@author: kevin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
arr1 = set(map(int, input().split()))

n2 = int(input())
arr2 = map(int, input().split())

print (len(arr1.difference(arr2)))