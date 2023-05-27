# -*- coding: utf-8 -*-
"""
Created on Sun May 28 00:28:34 2023

@author: kevin
"""

def average(array):
    s = set(array)
    res = sum(s)/len(s)
    
    return round(res,3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)