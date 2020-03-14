#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:25:29 2019

@author: mahya
"""

sequence1 = 'ABCDGH'
sequence2 = 'AGGTAB'
LCS = []

for element in sequence1:
    i = 0
    for elm in sequence2:
        if element == elm and i == 0:
            LCS.append(elm)
            sequence2 = sequence2.replace(elm, '')
            i = 1
            
            
print(len(LCS))
