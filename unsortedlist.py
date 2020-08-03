#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:46:00 2020

@author: mahya
"""


def max_product(unsortedlist):
    max_values = []
    product = 1
    
    while len(max_values)<3:
        max = 0
        for value in unsortedlist:
            if value > max and value not in max_values:
                max = value
        max_values.append(max)
        
    for value in max_values:
        product = value * product
    
    print(product)

unsorted_list = [3, 8, 5, 2, 12]
      
x = max_product(unsorted_list)
