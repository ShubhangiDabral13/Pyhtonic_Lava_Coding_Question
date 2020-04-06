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

        def middle_element(self):
            temp = self.head
            slow_temp = self.head
            if temp == None:
                print("There is no element in the linked list")
                return

            if temp.next == None:
                temp = temp.next
                print("the middle element in the linked list is {}".format(temp.data))
                return

            else:
                while(temp != None and temp.next !=  None):
                    #prev_slow = slow_temp
                    slow_temp = slow_temp.next
                    temp = temp.next.next
                print("The middle element in the linked list is {}".format(slow_temp.data))

        def display(self):
             temp = self.head
             while temp !=  None:
                 print(temp.data,end = " ")
                 temp  = temp.next



ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to display the middle element of the linked list
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        ll.middle_element()

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
