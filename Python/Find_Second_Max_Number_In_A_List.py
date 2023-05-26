# -*- coding: utf-8 -*-
"""
Created on Fri May 26 21:29:16 2023

@author: kevin
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
l = list(set(arr))
l.sort()
print (l[-2])
