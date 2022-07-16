class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        output = 0
        oneCount = 0
        zeroCount = 0
        for i in range(len(s)):
            if i > 0 and s[i-1] != s[i]:
                output += min(zeroCount, oneCount)
                if s[i] == '0':
                    zeroCount = 0
                else:
                    oneCount = 0
            if s[i] == '0':
                zeroCount += 1
            if s[i] == '1':
                oneCount += 1
        output += min(zeroCount, oneCount)
        return output