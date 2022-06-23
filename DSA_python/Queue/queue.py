'''
A queue is a data structure that contains an ordered set of data that follows a FIFO (first in, first out) protocol.

Now, we can use Python to build out a Queue class with those three essential queue methods:

enqueue() which will allow us to add a new node to the tail of the queue
dequeue() which will allow us to remove a node from the head of the queue and return its value
peek() which will allow us to view the value of head of the queue without returning it

'''

from DSA_python.LinkedList.node import Node

# Create the Queue class below:
class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

# Now we’ll make sure we aren’t attempting to peek() on an empty queue.
  def peek(self):
    if self.size == 0:
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size
# If there’s no max_size set, then we will always have space in the queue, so we can return True
  def has_space(self):
    if self.max_size != None:
      if self.max_size > self.size:
        return True
      else:
        return False
    else:
      return True

  def is_empty(self):
    if self.size == 0:
      return True
    else: 
      return False

  # enqueue is a fancy way of saying adding to the queue
  def enqueue(self, value):
# an if clause to check if the queue has space
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
# Check if the queue is empty
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
# Otherwise, use Node‘s set_next_node() method to: set item_to_add as the current tail‘s next node
      else:
        self.tail.set_next_node(item_to_add)
# set tail equal to item_to_add
        self.tail = item_to_add
# Increment the queue’s size by 1
      self.size += 1
    else:
      print("Sorry, no more room!")

  def dequeue(self):
# Add an if clause to check if the queue is not empty
    if self.get_size() > 0:
# If so, set a new variable item_to_remove to the current head
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
# Inside the if statement, below your print statement, check if the size is 1.
      if self.get_size() == 1:
# If so, give the queue’s head and tail a value of None
        self.head = None
        self.tail = None
      else:
# Otherwise, set the queue’s head equal to the following node
        self.head = self.head.get_next_node()
# reduce the queue’s size by 1
      self.size -= 1
# return the value of item_to_remove
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")