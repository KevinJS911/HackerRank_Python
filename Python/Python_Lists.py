# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:39:03 2023

@author: kevin
"""

if __name__ == '__main__':
    N = int(input())
    s = []
    for i in range(N):
        command = list(map(str, input().split()))
        
        if (command[0] == 'print'):
            print (s)
        
        if (command[0]=='append'):
            s.append(int(command[1]))
        
        if (command[0]=='pop'):
            s.pop()
        
        if (command[0]=='insert'):
            s.insert(int(command[1]), int(command[2]))
        
        if (command[0]=='sort'):
            s.sort()
        
        if (command[0]=='reverse'):
            s.reverse()
        
        if (command[0]=='remove'):
            s.remove(int(command[1]))
        
        
    
