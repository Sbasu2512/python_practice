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
'''
Start by checking to see if there is a current tail to the list
If there is (meaning the list is not empty), then we want to reset the pointers at the tail of the list:
Set the current tail’s next node to the new tail
Set the new tail’s previous node to the current tail
Update the tail property to be the new tail
Finally, if there isn’t a current head to the list (meaning the list was empty):
Update the head property to be the new tail since that node will be both the head and tail
'''
def add_to_tail(self, new_value):
    # new tail node 
    new_tail = Node(new_value)
    # existing tail node
    current_tail = self.tail_node
    # check if there is current tail in our linked list
    if current_tail != None:
      # Set the current tail’s next node to new_tail
      current_tail.set_next_node(new_tail)
      # Set new_tail‘s previous node to the current tail
      new_tail.set_prev_node(current_tail)
    # otherwise if current_tail == None, set the list’s tail to the new_tail.
    self.tail_node = new_tail
    # Lastly, if the list doesn’t have a head, set the list’s head to the new tail.
    if self.head_node == None:
      self.head_node = new_tail

def remove_head(self):
    removed_head = self.head_node
    # Check if removed_head has no value. If so, that means there’s nothing to remove, so return None to end the method.
    if removed_head == None:
      return None
# otherwise, if removed_head has value i.e. head node exists. set the list’s head to removed_head‘s next node.
    self.head_node = removed_head.get_next_node()
# If the list still has a head, 
    if self.head_node:
      # set its previous node to None, since the head of the list shouldn’t have a previous node.
      self.head_node.set_prev_node(None)
      # Check if removed_head is equal to the list’s tail.
    if removed_head == self.tail_node:
  #  If so, call the .remove_tail() method
      self.remove_tail()
    return removed_head.get_value()