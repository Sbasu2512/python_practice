'''
a doubly linked list is a sequential chain of nodes, just like a singly linked list.

The difference between a doubly linked list and a singly linked list is that in a doubly linked list, the nodes have pointers to the previous node as well as the next node. This means that the doubly linked list data structure has a tail property in addition to a head property, which allows for traversal in both directions.

So the nodes we will use for our doubly linked list contain three elements:

A value
A pointer to the previous node
A pointer to the next node
'''

'''class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value'''

class Double_Linked_Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node
    
    def set_prev_node(self,prev_node):
        self.prev_node = prev_node
    
    def get_prev_node(self):
        return self.prev_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value