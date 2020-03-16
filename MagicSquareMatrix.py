#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:36:21 2020

@author: mahya
"""

import numpy as np
magic_matix_1 = np.array([[5, 3, 4], [1, 5, 8], [6, 4, 2]])
magic_matrix_2 = np.array([[8, 3, 4], [1, 5, 9], [6, 7, 2]])

print(magic_matix_1.shape)
magic_matrix_size = int(np.sqrt(magic_matix_1.size))

magic_transform_cost = 0
print(magic_matix_1[0][1])

for i in range(magic_matrix_size):
    for j in range(magic_matrix_size):
        if magic_matix_1[i][j] != magic_matrix_2[i][j]:
            magic_transform_cost += np.abs(magic_matix_1[i][j] - magic_matrix_2[i][j])
            
print(magic_transform_cost)
            

