# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:02:01 2023

@author: kevin
"""
from collections import Counter

n = input()
rooms = list(map( int, input().split()))

s = list(set(rooms))
unique_rooms= list(Counter(rooms).keys())
values = list(Counter(rooms).values())

print (unique_rooms[values.index(1)])
