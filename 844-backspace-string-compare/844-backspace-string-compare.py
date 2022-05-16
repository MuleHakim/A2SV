class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        myStack = []
        for i in s:
            if myStack and i=="#":
                myStack.pop()
            elif i=="#":
                continue
            else:
                myStack.append(i)
        a = "".join(myStack)
        myStack.clear()
        for i in t:
            if myStack and i=="#":
                myStack.pop()
            elif i=="#":
                continue
            else:
                myStack.append(i)
        b = "".join(myStack)
        return a==b