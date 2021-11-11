# Initialise the Node
class Node:
    def __init__(self, data=None):
        self.item = data
        # Just reasuring myself
        self.next = None
        self.prev = None
# Class for doubly Linked List

class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Insert Element to Empty list

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            #pull from parent class
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    # Insert element at the end
    # Copy most of previous segment
    def Insert_To_Next(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches Null
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None
    # Delete the elements from the end
    #Again repeat previous steps
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    # Traversing and Displaying each element of the list

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print( n.item)
                n = n.next
        print("\n")


# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.InsertToEmptyList(10)
# Insert the element at the end
NewDoublyLinkedList.Insert_To_Next(20)
NewDoublyLinkedList.Insert_To_Next(30)
NewDoublyLinkedList.Insert_To_Next(40)
NewDoublyLinkedList.Insert_To_Next(50)
NewDoublyLinkedList.Insert_To_Next(60)
# Display Data
NewDoublyLinkedList.Display()
# Delete elements from start
NewDoublyLinkedList.DeleteAtStart()
# Delete elements from end
NewDoublyLinkedList.delete_at_end()
NewDoublyLinkedList.delete_at_end()
# Display Data
NewDoublyLinkedList.Display()
