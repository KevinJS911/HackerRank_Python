# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:09:27 2023

@author: kevin
"""

n = int(input())
s = set(map(int, input().split()))

commands = int(input())
for i in range(commands):
    comm= (input().split())
    if (len(comm)==2):
        k = int(comm[1])
    
    if (comm[0] == 'pop'):
        s.pop()
    
    if (comm[0] == 'remove'):
        s.remove(k)
    
    if (comm[0] == 'discard'):
        s.discard(k)
    
print (sum(s))
