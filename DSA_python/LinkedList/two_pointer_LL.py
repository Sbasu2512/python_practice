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

'''
Pointers at Different Speeds

Consider the following problem:

Create a method that returns the middle node of a linked list.

For example, given the linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, the middle node would be the element with value 4.

Approaches
As before, it’s possible to find a solution by iterating through the entire list, creating a list representation,
and then returning the middle index. 
But, also as before, this can potentially take up lots of extra space:

create list
while the linked list has not been fully iterated through
  push the current element onto list
  move forward one node
return list[length / 2]

Instead, we can use two pointers to move through the linked list. 
The first pointer takes two steps through the linked list for every one step that the second takes, so it iterates twice as fast:

fast pointer = linked list head
slow pointer = linked list head
while fast pointer is not None
  move fast pointer forward
  if the end of the linked list has not been reached
    move fast pointer forward
    move slow pointer forward
return slow pointer

When the first pointer reaches the end of the list, the “slower” second pointer will be pointing to the middle element. 
Let’s visualize the steps of the algorithm:

Starting State

F
S
1  2  3  4  5  6  7
First Tick

      F
   S
1  2  3  4  5  6  7
Second Tick

            F
      S
1  2  3  4  5  6  7
Third Tick

                  F
         S
1  2  3  4  5  6  7
Final Tick

                     F
         S
1  2  3  4  5  6  7  None

As long as we always move the fast pointer first and check to see that it is not None before moving it and the slow pointer again, 
we’ll exit iteration at the proper time and have a reference to the middle node with the slow pointer.
'''
# In Python, we can implement the find-middle function as such:
def find_middle(linked_list):
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if fast:
      fast = fast.get_next_node()
      slow = slow.get_next_node()
  return slow

#   Another equally valid solution is to move the fast pointer once with each loop iteration 
# but only move the slow pointer every-other iteration:

def find_middle_alt(linked_list):
  count = 0
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast:
    fast = fast.get_next_node()
    if count % 2 != 0:
      slow = slow.get_next_node()
    count += 1
  return slow