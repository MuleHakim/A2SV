class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        output = ""
        
        for i in s:
            if i == "(":
                stack.append([])
            elif i == ")":
                stack[-1].reverse()
                if len(stack) > 1:
                    last = stack.pop()
                    stack[-1] += last
            else:
                stack[-1].append(i)
                
        for j in range(len(stack[0])):
            output += stack[0][j]
            
        return output
