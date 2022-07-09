class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numS = str(num)
        output = 0
        i = 0
        while i<=len(numS)-k:
            if int(numS[i:i+k])!=0 and num%int(numS[i:i+k])==0:
                output += 1
            i += 1
        return output