# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:35:56 2023

@author: kevin
"""

if __name__ == '__main__':
    s = input()
    a=[0,0,0,0,0]
    for i in range(len(s)):
        if (s[i].isalnum()):
            a[0] +=1
        
        if (s[i].isalpha()):
            a[1] +=1
        
        if (s[i].isdigit()):
            a[2] += 1
        
        if (s[i].islower()):
            a[3] +=1

        if (s[i].isupper()):
            a[4] +=1
    for j in range(5):
        if (a[j]>0):
            print (True)
        else:
            print (False)
    

        
