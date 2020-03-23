"""
Algorithm for Next_Greater_Number
* Push the first element to stack.
* Pick rest of the elements one by one and follow the following steps in loop.
  1. Mark the current element as next.
  2. If stack is not empty, compare top element of stack with next.
  3. If next is greater than the top element,Pop element from stack. next is the next greater element for the popped element.
  4. Keep popping from the stack while the popped element is smaller than next. next becomes the next greater element for all
  such popped elements Finally, push the next in the stack.
* After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
"""

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def check(arr):
    s1 = createStack()
    push(s1,arr[0])

    for i in range(1,len(arr)):
        element = pop(s1)
        next = arr[i]
        while element<next:
            print("{} --- {}".format(element,next))
            if len(s1) == 0:
                break
            else:
                element =pop(s1)
        if element>next:
            push(s1,element)
        push(s1,next)

    while len(s1) != 0:
        print("{} --- -1".format(pop(s1)))

arr = [11,13,21,3]
check(arr)
