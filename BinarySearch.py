#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:17:31 2019

@author: mahya
"""
def binarySearch(sortedArray, start, end, data):
    if end >= 1:
        mid = int(start + (end - start)/2)
        
        if sortedArray[mid] == data:
            return mid
        elif sortedArray[mid] < data:
            return binarySearch(sortedArray, mid+1, end, data)
        elif sortedArray[mid] > data:
            return binarySearch(sortedArray, start, mid-1, data)
        else:
            return -1
        
        
   
    
    
sortedArray = [2, 3, 4, 10, 40]
item = 10

result = binarySearch(sortedArray, 0, len(sortedArray)-1, item)
print(result)