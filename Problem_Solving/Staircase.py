# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:49:59 2023

@author: kevin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        print (" "*(n-i)+'#'*i)
    
    return 0
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
