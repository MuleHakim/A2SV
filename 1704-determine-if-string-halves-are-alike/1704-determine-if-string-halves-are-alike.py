class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        left = 0
        right = 0
        vowels = "aeiouAEIOU"
        for i,j in zip(s1,s2):
            if i in vowels: left += 1
            if j in vowels: right += 1
        return left==right