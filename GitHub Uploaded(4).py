#!/usr/bin/env python
# coding: utf-8

# ##
# Linked Lists
# 
# Formation of Linked List,------->     Addition  of Linked List at the begening and ------->     Addition  of Linked List at the ending##

# In[ ]:


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class Linked_List:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        n=self.head
        while n is not None:
            print(n.data) 
            n = n.ref
    def add_begning(self, new):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_ending(self):
        new_node = Node(data)
        self.head = n
        if n is None:
            n =new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
                
        

