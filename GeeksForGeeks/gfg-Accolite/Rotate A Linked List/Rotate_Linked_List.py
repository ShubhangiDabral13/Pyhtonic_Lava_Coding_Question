"""
To rotate the linked list, we need to change next of kth node to NULL, next of the last node to the previous head node, and finally,
 change head to (k+1)th node. So we need to get hold of three nodes: kth node, (k+1)th node and last node.
Traverse the list from the beginning and stop at kth node. Store pointer to kth node. We can get (k+1)th node using kthNode->next.
 Keep traversing till the end and store pointer to last node also. Finally, change pointers as stated above.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head  ==  None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def rotate(self,k):
        temp = self.head
        if temp == None:
            print("Linked list does not have any element")
            return
        count = 0
        while(count < k and temp != None):
            temp = temp.next
            count += 1
        if temp == None:
            return
        k_temp = temp
        while(temp.next != None):
            temp = temp.next
        temp.next = self.head
        self.head = k_temp.next
        k_temp.next = None

    def display(self):
        temp = self.head
        while temp !=  None:
            print(temp.data,end = " ")
            temp  = temp.next


ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to rotate a linked List
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = int(input())
        ll.insert(a)

    elif ch == 2:
        a = int(input("Enter the index in linked_List from where you want to rotate"))
        ll.rotate(a)

    elif ch == 3:

        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
