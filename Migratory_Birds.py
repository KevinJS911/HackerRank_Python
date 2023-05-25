#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    
    counts = []
    val = list(set(arr))
    for i in range(len(val)):
        counts.append(arr.count(val[i]))
    
    maxValues = []
    for i in range(len(val)):
        if (counts[i]==max(counts)):
            maxValues.append(val[i])            
    
    return min(maxValues)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
