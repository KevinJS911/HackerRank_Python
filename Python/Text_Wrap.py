# -*- coding: utf-8 -*-
"""
Created on Mon May 29 00:45:21 2023

@author: kevin
"""
import textwrap

def wrap(string, max_width):
    l = list(string)
    strLength = len(l)
    
    res = []
    for i in range(0, strLength, max_width):
        res.append("".join(l[i:i+max_width])+"\n")
    
    return ''.join(res)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)