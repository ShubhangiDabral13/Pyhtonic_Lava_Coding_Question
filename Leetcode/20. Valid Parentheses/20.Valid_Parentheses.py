class Solution:
    def isValid(self, s: str) -> bool:
        closed_parentheses = [")","]","}"]
        open_parentheses = ["(","[","{"]
        stack = []
        if len(s)%2 != 0:
            return False
        for i in s:
            if i in open_parentheses:
                stack.append(i)
            elif i in closed_parentheses:
                pos = closed_parentheses.index(i)
                if(len(stack) != 0 and open_parentheses[pos]== stack[-1]):
                    a = stack[-1]
                    stack.remove(a)
        if len(stack) == 0:
            return True
        else:
            return False
                
