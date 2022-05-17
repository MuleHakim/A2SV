class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in s:
            if ord(i)<97 and i.isalpha():
                s = s.replace(i,chr(ord(i)+32))
        return s