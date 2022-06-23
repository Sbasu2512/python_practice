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
    new_tail = Double_Linked_Node(new_value)
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
'''
Start by checking if there’s a current head to the list.
If there isn’t, the list is empty, so there’s nothing to remove and the method ends
Otherwise, update the list’s head to be the current head’s next node
If the updated head is not None (meaning the list had more than one element when we started):
Set the head’s previous node to None since there should be no node before the head of the list
If the removed head was also the tail of the list (meaning there was only one element in the list):
Call .remove_tail() to make the necessary changes to the tail of the list (we will create this method in the next exercise!)
Finally, return the removed head’s value
'''
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
'''
Start by checking if there’s a current tail to the list.
If there isn’t, The list is empty, so there’s nothing to remove, and the method ends
Otherwise, update the list’s tail to be the current tail’s previous node
If the updated tail is not None (meaning the list had more than one element when we started):
Set the tail’s next node to None since there should be no node after the tail of the list
If the removed tail was also the head of the list (meaning there was only one element in the list):
Call .remove_head() to make the necessary changes to the head of the list
Finally, return the old tail’s data
'''
def remove_tail(self):
    removed_tail = self.tail_node
# Check if removed_tail has no value. If so, i.e., the list is empty and there’s nothing to remove, 
# so return None to end the method.
    if removed_tail == None:
      return None
# otherwise, if removed_tail has value. set the list’s tail to removed_tail‘s previous node.
    self.tail_node = removed_tail.get_prev_node()
# If the list still has a tail
    if self.tail_node != None:
# set the tail’s next node to None, since the tail of the list shouldn’t have a next node.
      self.tail_node.set_next_node(None)
# If the removed tail was also the head of the list (meaning there was only one element in the list):
    if removed_tail == self.head_node:
# Call .remove_head() to make the necessary changes to the head of the list
      self.remove_head()
# Finally, return the old tail’s data
    return removed_tail.get_value()
    
def remove_by_value(self, value_to_remove):
    node_to_remove = None
# a current_node node and set it equal to the list’s head. 
# Then create a while loop that runs while current_node isn’t None
    current_node = self.head_node
# Inside the while loop, but before you updated current_node to be its next node, 
# create an if statement that checks if current_node‘s value matches the passed in value_to_remove. 
# If it does, that means we have found the matching node.
# Inside the if:
# Set node_to_remove to current_node
# break to leave the while loop, since we don’t need to keep looking through the list
    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
      current_node = current_node.get_next_node()
# Outside your while loop, check if node_to_remove has any value. 
# If it doesn’t, that means there was no matching node in the list, so return None to end the method.
    if node_to_remove == None:
      return None
# check if node_to_remove is the list’s head. If so, call .remove_head().
    if node_to_remove == self.head_node:
      self.remove_head()
# if node_to_remove is the list’s tail, call .remove_tail()
    if node_to_remove == self.tail_node:
      self.remove_tail()
    else:
# A next_node node that is equal to node_to_remove‘s next node
      next_node = node_to_remove.get_next_node()
# A prev_node node that is equal to node_to_remove‘s previous node
      prev_node = node_to_remove.get_prev_node()
# Now that we have our nodes, we can remove the pointers to and from node_to_remove and have next_node and prev_node point to each other. Still in the else block:
# Set next_node‘s previous node to prev_node
# Set prev_node‘s next node to next_node 
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    return node_to_remove
