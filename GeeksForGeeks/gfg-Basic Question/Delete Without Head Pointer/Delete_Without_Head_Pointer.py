class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert(data,head_ref):
    new_node = Node(data)
    new_node.next = head_ref
    head_ref = new_node

    return head_ref

def display(head):
    temp = head
    while(temp != None):
        print(temp.data,end= " ")
        temp = temp.next

def deletenode(ptr):
    temp = ptr.next
    ptr.data = temp.data
    ptr.next = temp.next


if __name__ == '__main__':

    # Start with the empty list
    head = None

    # Use push() to construct below list
    # 1->12->1->4->1
    head = insert(1, head)
    head = insert(4, head)
    head = insert(1, head)
    head = insert(12, head)
    head = insert(1, head)

    print("Before deleting ")
    display(head)

    # I'm deleting the head itself.
    # You can check for more cases
    deletenode(head)

    print("\nAfter deleting")
    display(head)     
