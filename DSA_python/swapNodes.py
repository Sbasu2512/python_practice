from node import Node
from linkedList import LinkedList

def swap_nodes(input_list, val1, val2):
  print(f'Swapping {val1} with {val2}')
# Finding the Matching and Preceding Nodes
# We will start by setting node1 equal to the head of the list, and then creating a while loop that runs while node1 isn’t None. 
# Inside the loop, we will check if node1‘s value matches val1. 
# If so, we break out of the loop as we have found the correct node. 
# If there is no match, we update node1_prev to be node1 and move node1 to its next node
  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return
# we have found our matching node, and also saved its previous node
  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return
# Our next step is to set node1_prev and node2_prev‘s next nodes, starting with node1_prev. 
# We’ll begin by checking if node1_prev is None. 
# If it is, then the node1 is the head of the list, and so we will update the head to be node2. 
# If node1_prev isn’t None, then we set its next node to node2
  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)