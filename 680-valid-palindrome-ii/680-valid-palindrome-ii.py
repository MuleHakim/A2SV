class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                temp1 = s[i:j]
                temp2 = s[i+1:j+1]
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]
            i += 1
            j -= 1
        return True