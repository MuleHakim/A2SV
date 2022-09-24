class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        res = math.inf
        i = 0
        j = 0
        tmp_total = nums[i]
        while i <= j and j < len(nums):
            if tmp_total < target:
                j += 1
                if j < len(nums):
                    tmp_total += nums[j]
            else:
                res = min(res, j-i + 1)
                tmp_total -= nums[i]
                i += 1
        return 0 if res == math.inf else res