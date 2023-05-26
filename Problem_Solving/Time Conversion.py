# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:51:10 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if (s[-2]=='A'):
        if (s[:2]=="12"):
            s = "00"+s[2:]        
    else:
        if (int(s[:2])<12):
            s = str(int(s[:2])+12)+s[2:]
    return s[:-2]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
