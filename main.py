# program to reverse a linked list
#initialize a node
class Node:
    def __init__(self,data):
        # Constructor to initialize the node object
        self.data=data
        self.head=None
# initialize a linked list
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # function to add a new node at the front
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # a function to reverse a linked list
    # introduce 3 place holders one as a head and the other to interchange
    def reverse(self):
        prev = None
        current = self.head
        temp=None
        # use a while loop until current is null
        while current!=None:
            temp= current.next
            current.next = prev
            prev = current
            current=temp
        self.head=prev
    # a function to print the linked list
    def printList(self):
        itr=self.head
        while itr:
            print(itr.data, end="-->")
            itr=itr.next
# a driving code
llist=LinkedList()

llist.push(45)
llist.push(34)
llist.push(25)
llist.push(67)
print("Original linked list:")
llist.printList()
print("\n""reversed linked list")
llist.reverse()
llist.printList()




