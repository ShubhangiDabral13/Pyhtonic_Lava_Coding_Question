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

        def ispallindrome(self,str):
            if str == str[::-1]:
                return True
            else:
                return False

        def pallindrome(self):
            ans = []
            temp = self.head
            if temp == None:
                print("Linked list is empty")
            else:
                while(temp !=None):
                    ans.append(temp.data)
                    temp = temp.next
            str = "".join(ans)
            return(self.ispallindrome(str))

        def display(self):
            temp = self.head
            while temp !=  None:
                print(temp.data,end = " ")
                temp  = temp.next

ll = Linked_List()
ch = 0
while(ch != 4):
    print("""Enter 1 to insert a node at front in Linked_List
    Enter 2 to check whether Linked list is pallindrome or not
    Enter 3 to print the linked List
    Enter 4 to to quit """)
    ch = int(input())
    if ch == 1:
        print("Enter the data you want to insert in the linked list")
        a = input()
        ll.insert(a)

    elif ch == 2:
        print(ll.pallindrome())

    elif ch == 3:
        ll.display()

    elif ch == 4:
        print("We will quit")

    else:
        print("Wrong choice")
