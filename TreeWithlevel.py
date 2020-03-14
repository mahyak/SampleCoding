#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:49:11 2019

@author: mahya
"""
class Node:
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None
        
    
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.item)
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)
            
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
        
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
    if (lheight > rheight):
        return lheight + 1
    else:
        return rheight + 1
            
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)