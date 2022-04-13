class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)-1):
            while ((nums[i-1] + nums[i+1]) / 2 == nums[i] and i > 0):
                nums[i],nums[i+1] = nums[i+1],nums[i]
                i = i - 1
                
        return nums
               
