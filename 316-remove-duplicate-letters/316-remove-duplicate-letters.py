class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)        
        
        # s = list(s)
        # i = 0
        # while i<len(set(s))-1:
        #     if s[i] in s[i+1:]:
        #         s.remove(s[i])
        #         i = 0
        #     else:
        #         i += 1
        # output = sorted(''.join(s))
        # return ''.join(output)