#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 10:29:37 2020

@author: mahya
"""

#Lowest Common Ancestor in a Binary Tree

# first we need to make the tree
# find the path for each value
# compare the path to find the least common ancestor


class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        
def find_path(root, path, value):
    
    if root is None:
        return False
    
    path.append(root.key)
    
    if (root.key == value):
        return True
    
    if ((root.left != None and find_path(root.left, path, value)) or 
        (root.right != None and find_path(root.right, path, value))):
        return True
    
    path.pop()
    return False
    
def find_least_ancestor(root, value1, value2):
    path1 = []
    path2 = []
    
    find_path(root, path1, value1)
    find_path(root, path2, value2)
    
    length = 0
    
    if len(path1)>=len(path2):
        length = len(path2)
    else:
        length = len(path1)
    
    minimum_anc = root.key
    
    for i in range(0, length):
        if path1[i] == path2[i]:
            minimum_anc = path1[i]
            
    return  minimum_anc
        
        
    
    
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.roght = Node(7)

print(find_least_ancestor(root, 5, 7))




        
        
    
      