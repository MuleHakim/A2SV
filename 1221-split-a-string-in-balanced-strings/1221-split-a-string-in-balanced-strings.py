class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        tmp = 0
        for i in s:
            if i=="R":
                tmp += 1
            if i=="L":
                tmp -= 1
            if tmp==0:
                output += 1
        return output