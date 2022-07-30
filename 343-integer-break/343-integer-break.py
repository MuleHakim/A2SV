class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]=max(dp[i], (i-j)*j )
                dp[i]=max(dp[i], j*dp[i-j])  
        return dp[n] 