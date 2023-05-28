# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:40:42 2023

@author: kevin


 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
arr1 = set(map(int, input().split()))

commands = int(input())
x = arr1
for i in range(commands):
    comm = list(map(str, input().split()))
    
    arr2 = set(map(int, input().split()))

    
    if (comm[0]=='intersection_update'):
        x = x.intersection(arr2)

    if (comm[0]=='symmetric_difference_update'):
        x = x.symmetric_difference(arr2)

    if (comm[0]=='difference_update'):
        x = x.difference(arr2)

    if (comm[0]=='update'):
        x.update(arr2)

print (sum(x))