from double_ll_node import Double_Linked_Node
'''

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