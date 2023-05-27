# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:23:03 2023

@author: kevin
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):

    ave= sum(bill)/2

    bill.pop(k)

    ave_wo_Anna = sum(bill)/2

    if (b == ave_wo_Anna):
        print ("Bon Appetit")
    else:
        print (int(ave - ave_wo_Anna))

    return 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
