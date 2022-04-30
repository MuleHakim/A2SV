class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n==0:
            return 1
        elif n==1:
            return x
        else:
            return pow(x,n)
                
