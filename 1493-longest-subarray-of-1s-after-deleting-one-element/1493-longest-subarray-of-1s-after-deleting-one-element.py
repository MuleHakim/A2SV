class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count, j = 0, 0
        for i in range(len(nums)):
            count += (nums[i] == 0)
            if count >= 2:
                count -= (nums[j] == 0)
                j += 1
        return i-j