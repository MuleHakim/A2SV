class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        myStack = [0]
        for i in s:
            if i == '(':
                myStack.append(0)
            else:
                p = myStack.pop()
                myStack[-1] += max(2*p, 1)
        return myStack.pop()