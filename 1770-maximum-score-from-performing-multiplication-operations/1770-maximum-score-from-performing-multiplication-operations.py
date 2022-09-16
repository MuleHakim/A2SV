class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j] = max(multipliers[i] * nums[j] + dp[i + 1][j + 1], multipliers[i] * nums[n-1-(i-j)] + dp[i+1][j])
        return dp[0][0]
