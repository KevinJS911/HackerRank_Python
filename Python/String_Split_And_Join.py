# -*- coding: utf-8 -*-
"""
Created on Mon May 29 00:41:58 2023

@author: kevin
"""

def split_and_join(line):
    res = list(line.split(" "))
    return "-".join(res)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)