class Solution:
    def concatenatedBinary(self, n: int) -> int:
        tmp = ""
        for i in range(1,n+1):
            tmp += bin(i).replace("0b","")
        return int(tmp,2) % (10**9 + 7)