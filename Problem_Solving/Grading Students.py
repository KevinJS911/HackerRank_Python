# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:51:23 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    output = []
    for i in range(len(grades)):
        if (grades[i] < 38):
            output.append(grades[i])
    
        elif (grades[i]%5>=3 and grades[i]>=38):
            grades[i]+= 5 - grades[i]%5
            output.append(grades[i])
        else:
            output.append(grades[i])
    
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
