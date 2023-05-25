# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:48:22 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l2r = 0
    r2l = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i ==j):
                l2r += arr[i][j]
            if (i+j+1== len(arr)):
                r2l += arr[i][j]
    
    return abs(l2r-r2l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
