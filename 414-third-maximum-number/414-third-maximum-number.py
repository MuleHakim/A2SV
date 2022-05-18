class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        nums = sorted(nums,reverse=True)
        output = 0
        i = 0
        while i<len(nums):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            else:
                i += 1
                output += 1
                if output==3:
                    return nums[i-1]
        return max(nums)
    