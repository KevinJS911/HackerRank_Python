# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:33:46 2023

@author: kevin
"""

m = int(input())
arr1 = set(map(int, input().split()))

n = int(input())
arr2 = set(map(int, input().split()))

diff1 =(arr1.difference(arr2))
diff1.update(arr2.difference(arr1))

li = list(diff1)
li.sort()
for i in range(len(li)):
    print (li[i])