# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:50:13 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    smallest = arr[0]
    largest = arr[0]
    for i in range(len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
        if (arr[i] > largest):
            largest = arr[i]
    
    mini = sum(arr)- largest
    maxi = sum(arr) - smallest
            
    print (str(mini) +" "+str(maxi))
    
    return 0
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
