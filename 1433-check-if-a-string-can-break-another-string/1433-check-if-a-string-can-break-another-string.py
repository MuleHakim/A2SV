class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = [i for i in s1]
        s1.sort()
        s2 = [i for i in s2]
        s2.sort()
        tmp1 = True
        tmp2 = True
        n = len(s1)
        for i in range(n):
            if not (s1[i]>=s2[i]):
                tmp1 = False
                break
        for i in range(n):
            if not (s2[i]>=s1[i]):
                tmp2 = False
                break
        return tmp1 + tmp2