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
                slow_temp = slow_temp.next
                temp = temp.next.next
                if(temp == slow_temp):
                    self.removeloop(slow_temp)
                    return (1)
            return(0)

        def removeloop(self,slow_temp):
            ptr1 = self.head
            while True:
                ptr2 = slow_temp
                while(ptr2.next != ptr1 and ptr2.next != slow_temp):
                    ptr2 = ptr2.next

                if ptr2.next == ptr1:
                    break

                ptr1 = ptr1.next

            ptr2.next = None


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
print("linked list after removing loop")
llist.display()
