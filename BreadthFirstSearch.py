#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:52:15 2019

@author: mahya
"""
from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def BFS(self, startpoint):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(startpoint)
        visited[startpoint]=True
        
        while (queue):
            startpoint = queue.pop(0)
            print(startpoint)
            
            for i in self.graph[startpoint]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
        
        
        
g = Graph()
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.BFS(2)