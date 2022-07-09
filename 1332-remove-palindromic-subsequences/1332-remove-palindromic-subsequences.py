class Solution:
    def removePalindromeSub(self, s: str) -> int:
        for i in range(len(s)//2):
            if s[i] != s[-i - 1]:
                return 2
        return 1