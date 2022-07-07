class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums)==1:
            if nums[0]==0:
                return 1
            return 0
        else:
            if nums[0]!=0:
                return 0
            if nums[-1]!=len(nums):
                return len(nums)
            for i in range(len(nums)-1):
                if nums[i+1] - nums[i] > 1:
                    return nums[i] + 1
            return len(nums)