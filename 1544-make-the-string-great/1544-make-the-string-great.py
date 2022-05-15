class Solution:
    def makeGood(self, s: str) -> str:
        myStack = []
        for i in s:
            if myStack and myStack[-1]!=i and i.lower()==str(myStack[-1]).lower():
                myStack.pop()
            else:
                myStack.append(i)
        return "".join(myStack)
        