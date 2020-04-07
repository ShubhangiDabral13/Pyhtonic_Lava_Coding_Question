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

    def sortlist(self):
        count = [0,0,0]
        temp = self.head
        while(temp != None):
            count[temp.data] += 1
            temp = temp.next
        i = 0
        temp  = self.head
        while(temp != None):
            if count[i] == 0:
                i += 1
            else:
                temp.data = i
                count[i] -= 1
                temp  = temp.next

    def display(self):
        temp = self.head
        while temp !=  None:
            print(temp.data,end = " ")
            temp  = temp.next


llist = Linked_List()
llist.insert(0)
llist.insert(1)
llist.insert(0)
llist.insert(2)
llist.insert(1)
llist.insert(1)
llist.insert(2)
llist.insert(1)
llist.insert(2)

print("Linked List before sorting")
llist.display()

llist.sortlist()

print("\nLinked List after sorting")
llist.display()
