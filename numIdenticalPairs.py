class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)
        numGoodArray = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    numGoodArray += 1
        return numGoodArray
                    
