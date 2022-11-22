class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(0, int(sqrt(n)) + 1)]
        numsSet = set(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i in numsSet:
                dp[i] = 1
                continue
            for num in nums:
                if num >= i:
                    break
                dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[-1]