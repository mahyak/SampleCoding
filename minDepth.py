#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 08:02:07 2020

@author: mahya
"""

class  Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
def minDepth(root):
    
    if root is None:
        return 0
        
    q = []
    q.append({"node": root, "depth": 1})
        
    while (len(q)>0):
        queueItem = q.pop(0)
        node = queueItem['node']
        depth = queueItem['depth']
            
        if node.right is None and node.left is None:
            return depth
            
        if node.right is not None:
            q.append({"node": node.right, "depth": depth+1})
            
        if node.left is not None:
            q.append({"node": node.left, "depth": depth+1})
                
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

print(minDepth(root))

                
        