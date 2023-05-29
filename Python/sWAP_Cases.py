# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:05:34 2023

@author: kevin
"""

def swap_case(s):
    l = list(s)
    res= []
    
    for i in range(len(l)):
        if (l[i].isupper()==True):
           res.append(l[i].lower())
        else:
            res.append(l[i].upper())
    
    return ''.join(res)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)