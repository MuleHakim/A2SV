class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-2
        total = 0
        while i<=j:
            total += min(nums[i],nums[i+1])
            i += 2
        return total