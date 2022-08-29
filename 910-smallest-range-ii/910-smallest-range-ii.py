class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        output = nums[-1]-nums[0]
        for i in range(len(nums)-1):
            output = min(output, max(nums[-1]-k, nums[i]+k)- min(nums[0]+k, nums[i+1]-k))
        return output