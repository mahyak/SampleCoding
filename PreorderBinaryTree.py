#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:35:28 2020

@author: mahya
"""


def canReperesentPBT(pre):
    
    root = 0
    s = []
    
    for element in pre:
        
        if element<root:
            return False
            
        while(len(s) > 0 and s[-1] < element):
            root = s.pop()
            
        s.append(element)
        
    return True

pre1 = [40 , 30 , 35 , 20 ,  80 , 100]
pre2 = [40 , 30 , 35 , 20 ,  80 , 100]

print(canReperesentPBT(pre1))
print(canReperesentPBT(pre2))