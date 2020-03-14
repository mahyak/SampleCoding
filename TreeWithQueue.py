#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:55:37 2019

@author: mahya
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
def printLevelTree(root):    
    queue = []
    queue.append(root)
    while (len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

printLevelTree(root)