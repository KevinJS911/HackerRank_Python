# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:15:42 2023

@author: kevin
"""
def mutate_string(string, position, character):
    out = string[:position]+character+string[position+1:]
    
    return out

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)