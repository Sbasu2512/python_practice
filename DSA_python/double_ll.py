from double_ll_node import Double_Linked_Node
'''
the nodes have pointers to the previous node as well as the next node. This means that the doubly linked list data structure has a tail property in addition to a head property, which allows for traversal in both directions.

So the nodes we will use for our doubly linked list contain three elements:

A value
A pointer to the previous node
A pointer to the next node

For our use, we want to be able to:

Add a new node to the head (beginning) of the list
Add a new node to the tail (end) of the list
Remove a node from the head of the list
Remove a node from the tail of the list
Find and remove a specific node by its value
Print out the nodes in the list in order from head to tail
'''
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

'''Since a doubly linked list has an additional tail property and is built with nodes that each have two pointers, 
there are a few more steps:

Start by checking to see if there is a current head to the list
If there is (meaning the list is not empty), then we want to reset the pointers at the head of the list:
Set the current head’s previous node to the new head
Set the new head’s next node to the current head
Update the head property to be the new head
Finally, if there isn’t a current tail to the list (meaning the list was empty):
Update the tail property to be the new head since that node will be both the head and tail of the list'''

def add_to_head(self, new_value):
    # new head which is being added
    new_head = Double_Linked_Node(new_value)
    # current head => existing head
    current_head = self.head_node

    if current_head != None:
      # setting existing head's prev pointer to new head
      current_head.set_prev_node(new_head)
      # setting new head's next pointer to existing head
      new_head.set_next_node(current_head)
# setting new head and as the head_node
    self.head_node = new_head
# checking if tail node exists or not, if not then setting new_head as the tail node as well
    if self.tail_node == None:
      self.tail_node = new_head