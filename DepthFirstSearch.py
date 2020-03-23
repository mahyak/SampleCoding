#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:08:45 2020

@author: mahya
"""

from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
                
    def DFS(self):
        length = len(self.graph)
        visited = [False] * length
        
        for i in range(length):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                
g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS() 

