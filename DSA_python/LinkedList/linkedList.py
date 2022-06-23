from DSA_python.node import Node


from node import Node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  # get the head_node from where the linkedlist will start
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:
# insert a new head_node
  def insert_beginning(self,new_value):
    new_node = Node(new_value)
    # new_node.next_node = self.head_node
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

# The method should traverse the list, beginning at the head node, and collect each node’s value in a string. 
# Once the end of the list has been reached, the method should return the string.
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

#   we’ll create a function that removes the first node that contains a particular value.
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

