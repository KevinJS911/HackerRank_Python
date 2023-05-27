# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:22:19 2023

@author: kevin
"""

def count_substring(string, sub_string):
    
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)]==sub_string):
            count +=1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)