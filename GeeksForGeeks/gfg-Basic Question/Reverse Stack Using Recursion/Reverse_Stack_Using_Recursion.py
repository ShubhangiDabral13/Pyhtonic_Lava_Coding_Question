#To reverse a stack by recursion 
def reverse(stack):
    if stack != []:
        print(stack.pop())
        return reverse_stack(stack)
    else:
        return

stack = [12,64,2,7,0,3,13,13]
reverse_stack(stack)
