class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        res = 0
        i = 0
        for j,val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[i]
                i += 1
            res += j-i+1
        return res