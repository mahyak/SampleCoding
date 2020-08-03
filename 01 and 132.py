#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:19:38 2020

@author: mahya
"""

# ====================== 01 Matrix =================== #
import numpy as np

matrix_input = np.array([[0,0,0],[0,1,0],[1,1,1]])
dist = np.array()

row = np.size(matrix_input, 0) -1
col = np.size(matrix_input, 1) -1

for i in range(0, row):
    for j in range(0, col):
        if matrix_input[i, j] == 0:
            dist[i, j] = 0
        else:
            for k in range(0, row):
                for l in range(0, col):
                    if matrix_input[k,l] == 0:
                        dis = abs(k-i) + abs(l-j)
                        dist[i,j] = min(dist[i,j], dis)

                        
# ====================== 01 Matrix =================== #
input_list = [-1, 3, 2, 0]

length = len(input_list)-1

for i in range(0, length):
    for j in range(i+1, length+1):
        if (input_list[i] < input_list[j]):
            for k in range(j+1, length+1):
                if (input_list[j] > input_list[k] and input_list[i] < input_list[k] ):
                    print(input_list[i])
                    print(input_list[j])
                    print(input_list[k])

            

       
           

        
            
                        
          
                   
                
            




    
