class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = list(s)
        for i in range(len(s)):
            s_list.append(s_list.pop(0))
            if "".join(s_list)==goal:
                return True
        return False
        