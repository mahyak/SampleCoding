#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:44:30 2020

@author: mahya
"""


string  = "Ab,c,de!$"
position = 0
string_list = []
string_dic = {}
nonAlpha_position = []

for element in string:
    string_dic[position] = element
    
    if element.isalpha():
        string_list.append(element)
    else:
        nonAlpha_position.append(position)
        
    position += 1 

revers_string = []
count = 0

for i in range(len(string_list)):
    revers_string.append(string_list[len(string_list)-1-i])
        
for i in range(len(string)):
    if (i in nonAlpha_position):
        i +=1
    else:
        string_dic[i] = revers_string[count]
        count+=1
    
reverse_string = ''

for value in string_dic.values():
    reverse_string += value
    
print(reverse_string)