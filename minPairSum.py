class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxPair = nums[0]+nums[-1]
        for i in range(len(nums)//2):
            if nums[i]+nums[len(nums)-i-1] >= maxPair:
                maxPair = nums[i]+nums[len(nums)-i-1]  
        return maxPair
