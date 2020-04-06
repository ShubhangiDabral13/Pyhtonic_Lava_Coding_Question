"""
Floyd’s Cycle-Finding Algorithm: This is the fastest method and has been described below:

1).Traverse linked list using two pointers.
2).Move one pointer(slow_temp) by one and another pointer(temp) by two. 
3).If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop
"""

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

        def loop_present(self):
            temp = self.head
            slow_temp = self.head
            while (temp != None and slow_temp != None and temp.next != None):
                if(temp == slow_temp):
                    print("There is loop in the linked List")
                    return
                slow_temp = slow_temp.next
                temp = temp.next.next
            print("There is no loop in the linked List")



        def display(self):
            temp = self.head
            while temp !=  None:
                print(temp.data,end = " ")
                temp  = temp.next


llist = Linked_List()
llist.insert(20)
llist.insert(4)
llist.insert(15)
llist.insert(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head
llist.loop_present()
