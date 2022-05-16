class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k==1:
            return "0"
        if n==1:
            return "0"
        else:
            s = "0"
            for i in range(n-1):
                s = s + "1" + self.inverted(s)
            return s[k-1]
    def inverted(self,s):
        s = s.replace("1","2")
        s = s.replace("0","1")
        s = s.replace("2","0")
        s = s[::-1]
        return "".join(s)
        # s = list(s)
        # for i in range(len(s)):
        #     if s[0]=="0":
        #         s.pop(0)
        #         s.append("1")
        #     else:
        #         s.pop(0)
        #         s.append("0")
        # s = s[::-1]
        # return "".join(s) 
        