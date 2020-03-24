#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:55:45 2020

@author: mahya
"""

def search(arr, l, h, key):
    
    if (l>h):
        return -1
    
    mid = (l+h) // 2
    
    if arr[mid] == key:
        return mid
    
    if arr[l] <= arr[mid]:
        if key >= arr[l] and key<=arr[mid]:
            return search(arr, l, mid-1, key)
        return search (arr, mid+1, h, key)
        
    if key>=arr[mid] and key<=arr[h]:
        return search(arr, mid+1, l, key)
    return search(arr, l, mid-1, key)

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 6

result = search(arr, 0, len(arr)-1, key)
print(result)