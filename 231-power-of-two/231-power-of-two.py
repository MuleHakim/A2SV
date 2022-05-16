class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        ans = math.log2(n)
        if ans > 0 and ans==math.floor(ans):
            return True
        return False