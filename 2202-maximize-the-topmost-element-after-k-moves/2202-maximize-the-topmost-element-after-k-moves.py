class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            if k%2 == 0:
                return nums[0]
            else:
                return -1
        if k==0:
            return nums[0]
        if k==1:
            return nums[1]
        if k<len(nums):
            return max(nums[k],max(nums[:k-1]))
        if k==len(nums):
            return max(nums[:len(nums)-1])
        else:
            return max(nums)