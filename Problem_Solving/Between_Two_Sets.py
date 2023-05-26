# -*- coding: utf-8 -*-
"""
Created on Thu May 25 12:07:42 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    first =[]
    second = [] 
    for i in range(1,min(b)+1):
        flag1=[]
        for j in range(len(a)):
            if (i%a[j]==0):
                flag1.append(1)
        print(flag1)
        if (sum(flag1) == len(a)):
            first.append(i)
    print (first)

    for i in range(len(first)):
        flag2=[]
        for j in range(len(b)):
            print (first[i],b[j],b[j]%first[i]==0 )
            if (b[j]%first[i]==0):
                flag2.append(1)
        print(flag2)
        if (sum(flag2) == len(b)):
            second.append(first[i])
    
    return len(set(first).intersection(set(second)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
