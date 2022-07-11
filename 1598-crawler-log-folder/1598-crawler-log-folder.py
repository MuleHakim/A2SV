class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i=="../" and not stack:
                continue
            if i=="../" and stack:
                stack.pop()
                continue
            if i=="./":
                continue
            else:
                stack.append(i)
        return len(stack)