# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:46:52 2023

@author: kevin
"""

#%%Hello World

print ("Hello, World!")

#%%If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if (n%2==1):
        print ("Weird")
    elif (n>=2 and n<=5):
        print ("Not Weird")
    elif (n>=6 and n<=20):
        print ("Weird")
    else:
        print ("Not Weird")
        

#%%Python Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print (str(a+b))
    print (str(a-b))
    print (str(a*b))

#%%Python Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (str(a//b))
    print (str(a/b))

#%%Python Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print (str(i**2))

#%%Write a Function
def is_leap(year):
    leap = False
    if (year %4 == 0):
        leap = True
        if (year%100 ==0):
            leap = False
            if (year%400 ==0):
                leap =True 
        
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))

#%%Python Print
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end='')
