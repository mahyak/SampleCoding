#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:35:34 2019

@author: mahya
"""
# =============================================================================
# During the insertion process you have to be aware of the place of insertion
# At the begining
# In middle 
# At End
# =============================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.nextVal = None

class LinkedList:
    def __init__(self):
        self.headVal = None
    
    def printLinkedList(self):
        printVal = self.headVal
        
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.nextVal
            
    def inserttInSort(self, newVal):
        currentVal = self.headVal
        newNode = Node(newVal)
        
        while(currentVal is not None):
            prevVal = currentVal
            currentVal = currentVal.nextVal
            
            if (prevVal.data < newNode.data) and (newNode.data <= currentVal.data):
                prevVal.nextVal = newNode
                newNode.nextVal = currentVal
                return
        
        
linkedList = LinkedList()

linkedList.headVal = Node(2)

node2 = Node(5)
node3 = Node(7)
node4 = Node(10)
node5 = Node(15)

linkedList.headVal.nextVal = node2
node2.nextVal = node3
node3.nextVal = node4
node4.nextVal = node5
linkedList.printLinkedList()
linkedList.inserttInSort(8)
linkedList.printLinkedList()

