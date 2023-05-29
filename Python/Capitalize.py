# -*- coding: utf-8 -*-
"""
Created on Mon May 29 01:29:30 2023

@author: kevin
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = list(s)
    
    names[0]=names[0].upper()
    for i in range(len(names)):
        if (names[i]==" " and names[i+1].islower()):
            names[i+1]=names[i+1].upper()
    
    return ("".join(names))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
