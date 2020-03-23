#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:22:40 2020

@author: mahya

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def PrintList(self):
        temp = self.head
        
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next
            
    def deleteNode(self, data):
         temp = self.head
         
         if (temp.data == data):
             if (temp.next is not None):
                 temp.data = temp.next.data
                 temp.next = temp.next.next
             else:
                print("Can't delete the only node in the linked list")
                
         while (temp.next is not None and temp.next.data != data):
            temp = temp.next
            
         if temp.next is None:
            print("Can't delete it!")
         else:
            temp.next = temp.next.next
   

            
llist = LinkedList() 
llist.push(3) 
llist.push(2) 
llist.push(6) 
llist.push(5) 
llist.push(11) 
llist.push(10) 
llist.push(15) 
llist.push(12) 

print("Given Linked List: ", end = ' ') 
llist.PrintList() 
print("\n\nDeleting node 10:") 
llist.deleteNode(10) 
print("Modified Linked List: ", end = ' ') 
llist.PrintList() 
print("\n\nDeleting first node") 
llist.deleteNode(12) 
print("Modified Linked List: ", end = ' ') 
llist.PrintList() 