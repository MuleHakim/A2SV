class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        dict = {"(":")"}
        myStack = []
        temp = ""
        opeT = 0
        cloT = 0
        for i in range(len(s)):
            if s[i]=="(":
                opeT += 1
            else:
                cloT += 1
            temp += s[i]
            if temp and s[i]==")" and len(temp)%2==0 and dict[temp[0]]==temp[-1] and cloT==opeT:
                temp = temp[1:-1]
                myStack.append(temp)
                temp = list(temp)
                del(temp[::])
                temp = "".join(temp)
        return "".join(myStack)

        
        
#         dict = {"(":")"}
#         myStack = []
#         par = "()"
#         ans = ""
#         for i in s:
#             if i=="(":
#                 myStack.append(i)
#             else:
#                 myStack.pop()
#                 if myStack:
#                     ans += par
#         return ans
    