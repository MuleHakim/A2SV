class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = collections.Counter(s)
        for ch in s:
            if ch not in stack:
                while stack and ch <= stack[-1] and count[stack[-1]] > 1:
                    count[stack.pop()] -=1
                stack.append(ch)
            else:
                count[ch] -=1
        return "".join(stack)
