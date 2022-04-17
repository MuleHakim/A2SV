import math
import re
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1 = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or re.match("(-\w)",tokens[i]):
                stack1.append(int(tokens[i]))
            else:
                if tokens[i]=="+":
                    a = stack1.pop()
                    b = stack1.pop()
                    stack1.append(b+a)
                elif tokens[i]=="*":
                    a = stack1.pop()
                    b = stack1.pop()
                    stack1.append(b*a)
                elif tokens[i]=="-":
                    a = stack1.pop()
                    b = stack1.pop()
                    stack1.append(b-a)
                else:
                    a = stack1.pop()
                    b = stack1.pop()
                    if (a < 0 and b > 0) or ( a > 0 and b < 0):
                        stack1.append(math.ceil(b/a))
                    else:
                        stack1.append(b//a)
        return stack1.pop()
    
