# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:48:55 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    zero = 0
    neg = 0
    for i in arr: 
        if (i > 0 ):
            pos +=1
        elif (i==0):
            zero +=1
        else:
            neg += 1
    pos /= len(arr)
    zero /= len(arr)
    neg /= len(arr)
    
    print (format(round(pos,6), '0.6f'))
    print (format(round(neg,6), '0.6f'))
    print (format(round(zero,6), '0.6f'))
    
    return 0

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
