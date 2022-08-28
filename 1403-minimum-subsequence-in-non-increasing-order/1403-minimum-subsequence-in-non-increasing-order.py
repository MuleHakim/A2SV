class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            tmp = nums[:i+1]
            if sum(tmp)>sum(nums[i+1:]):
                return tmp