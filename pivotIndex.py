class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:])==0:
            return 0
        else:
            left = nums[0]
            right = sum(nums[1:])
            for i in range(1,len(nums)):
                right -= nums[i]
                if left == right:
                    return i
                left += nums[i]
            return -1
