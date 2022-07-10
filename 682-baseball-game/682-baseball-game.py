class Solution:
    def calPoints(self, ops: List[str]) -> int:
        myStack = []
        for i in range(len(ops)):
            if ops[i]=="D":
                myStack.append(2*myStack[-1])
            elif ops[i]=="C":
                myStack.pop(-1)
            elif ops[i]=="+":
                myStack.append(myStack[-1]+myStack[-2])
            else:
                myStack.append(int(ops[i]))
        return sum(myStack)