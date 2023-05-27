# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:49:36 2023

@author: kevin
"""

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print ("Hello "+first+" "+last+"! You just delved into python.")
    return 0

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)