class Solution:
    def decodeString(self, s: str) -> str:
        myStack = []
        on = 0
        for i in s:
            if i.isnumeric():
                if myStack and str(myStack[-1]).isnumeric() and on==0:
                    temp = myStack.pop()
                    myStack.append(temp+str(i))
                else:
                    myStack.append(str(i))
                    on = 0
            elif i.isalpha():
                myStack.append(i)
            elif i=="[":
                on = 1
                continue
            elif i=="]":
                x = myStack.pop()
                y = int(myStack.pop())
                z = y*x
                myStack.append(z)
            if len(myStack)>1 and str(myStack[-1]).isalpha() and str(myStack[-2]).isalpha():
                a = myStack.pop()
                b = myStack.pop()
                c = b + a
                myStack.append(c)
        return "".join(myStack) 