# Node data structure
class Node:
    def __init__(self, node_data=None, next=None):
        self.node_data = node_data
        self.next = next


# Main class
class LinkedList:
    def __init__(self):
        # set head to none initially
        self.head = None;

# insert a node at the head position
    def insert_at_first(self, node_data):
        node = Node(node_data, self.head)
        self.head = node

# insert a node at the last position
    def insert_at_last(self, node_data):
        if self.head is None:
            self.head = Node(node_data, None)
            return
        iterator = self.head
        # traverse until end
        while iterator.next:
            iterator = iterator.next

        # Now insert at the node at end
        iterator.next = Node(node_data, None)

    # insert a node at the particular position specified bu index position
    def insert_at_position(self, index, node_data):

        # check for validity of index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_first(node_data)
            return

        count = 0
        iterator = iterator = self.head

        while iterator:
            # traverse until an index before the insertion of node
            if count == index - 1:
                # create the node and insert in the actual position that is next node
                node = Node(node_data, iterator.next)
                iterator.next = node
                break

            iterator = iterator.next
            count += 1

# returns the length of the node
    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next

        return count

# prints the linked list
    def print_nodes(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iterator = self.head
        llstr = ""
        while iterator:
            llstr += str(iterator.node_data) + '-->'
            iterator = iterator.next
        print(llstr)

# remove node at the given index
    def remove_at_position(self, index):

        # check for validity of index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        iterator = iterator = self.head

        while iterator:
            # traverse until an index before the insertion of node
            # and replace it with the next to next node therby skipping the
            # immediate next node
            if count == index - 1:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count += 1

# client code
if __name__ == '__main__':
    lnklst = LinkedList()
    lnklst.insert_at_first(9)
    lnklst.insert_at_first(18)
    lnklst.insert_at_last(27)
    lnklst.insert_at_position(0, 9)
    lnklst.insert_at_position(2, 27)
    # lnklst.remove_at_position(2)
    
    lnklst.print_nodes()