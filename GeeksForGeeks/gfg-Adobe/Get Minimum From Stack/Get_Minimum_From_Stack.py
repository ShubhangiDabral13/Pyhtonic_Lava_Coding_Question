class Stack:
    def __init__(self):
        self.stack  = []
        self.spe_stack = []

    def push(self,a):
        self.stack.append(a)
        if self.spe_stack == []:
            self.spe_stack.append(a)
        elif self.stack[-1] <self.spe_stack[-1]:
            self.spe_stack.append(a)

    def pop(self):
        a = self.stack.pop()
        if a == self.spe_stack[-1]:
            self.spe_stack.pop()
        print("The element that have been poped out is {}".format(a))

    def getmin(self):
        print("The minimum element right now in the stack is {}".format(self.spe_stack[-1]))

    def display(self):
        for i in self.stack:
            print(i,end = " ")


s = Stack()
ch = 0
while ch != 5:
    print("""Enter 1 to push an element
    Enter 2 to pop an element
    Enter 3 to get minimum element
    Enter 4 to display element of the Stack
    Enter 5 to quit from it""")

    ch = int(input())

    if ch == 1:
        a = int(input("Enter the element you want to push "))
        s.push(a)

    elif ch == 2:
        s.pop()

    elif ch == 3:
        s.getmin()

    elif ch == 4:
        s.display()

    elif ch == 5:
        print("We will quit from it")

    else:
        print("You made a wrong choice")
