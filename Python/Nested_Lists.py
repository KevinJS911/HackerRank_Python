# -*- coding: utf-8 -*-
"""
Created on Fri May 26 21:41:47 2023

@author: kevin
"""
import numpy as np

name = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]
score = [37.21, 37.21,37.2,  41, 39]

#######Solution1
l = list(set(score))
l.sort()
secondLowest = l[1]
ind = np.where(np.array(score) == secondLowest)[0]

names = name[list(ind)]
for k in range(len(name)):
    if k in ind:
        print (name[k])

#######Solution 2
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        
    l = list(set(scores))
    l.sort()
    secondLowest = l[1]
    out =[]
    for k in range(len(scores)):
        if scores[k]==secondLowest:
            out.append(names[k])
    out.sort()
    for j in range(len(out)):
        print (out[j])
