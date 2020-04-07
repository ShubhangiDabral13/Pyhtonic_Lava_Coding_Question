class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
        def __init__(self):
            self.head = None

        def insert(self,data):
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node

        def swap_pairs(self):
            temp = self.head

            if temp == None:
                print("Link list is empty")
                return

            elif temp.next == None:
                print("Only one element in linkedlist")

            while(temp != None and temp.next !=  None):
                temp.data,temp.next.data = temp.next.data,temp.data
                temp = temp.next.next

        def display(self):
            temp = self.head
            while temp !=  None:
                print(temp.data,end = " ")
                temp  = temp.next


# Driver program
llist = Linked_List()
llist.insert(5)
llist.insert(4)
llist.insert(3)
llist.insert(2)
llist.insert(1)

print("Linked list before calling swap_pairs() ")
llist.display()

llist.swap_pairs()

print ("\nLinked list after calling swap_pairs()")
llist.display()
