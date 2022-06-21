'''
Two-Pointer Linked List Techniques

Two Pointers Moving in Parallel
Consider the following problem:

Create a method that returns the nth last element of a singly linked list.

For example: given a linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5, return the 2nd to last element. The answer would be element 4.

In order to do this, you’ll need some way of knowing how far you are from the end of the list itself.
However, in a singly linked list, there’s no easy way to iterate back through the list when you find the end.

we can solve this problem by using two pointers at different positions in the list but moving at the same rate. 
As in the previous example, we will use one pointer to iterate through the entire list, 
but we’ll also move a second pointer delayed n steps behind the first one. 
A count variable can keep track of the position of the current element in the linked list that the tail pointer is pointing to, 
which is initially set to 1 which is the first element’s position.

we will use one pointer to iterate through the entire list, but we’ll also move a second pointer delayed n steps behind the first one. 
A count variable can keep track of the position of the current element in the linked list that the tail pointer is pointing to, 
which is initially set to 1 which is the first element’s position.

The pseudocode for this approach would look like the following:

nth last pointer = None
tail pointer = linked list head
count = 1

while tail pointer exists
  move tail pointer forward
  increment count

  if count >= n + 1
    if nth last pointer is None
      set nth last pointer to head
    else
      move nth last pointer forward

return nth last pointer
'''

# In Python, we can implement the nth-last-node-finder function as such:

def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 1
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n + 1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current

'''
The exact variable names aren’t important, and the internal implementation could be written in a number of ways, 
but the important part is that we are able to complete this problem efficiently, in O(n) time 
(we must iterate through the entire list once), and O(1) space complexity 
(we always use only three variables no matter what size the linked list is: two pointers and a counter).
'''

