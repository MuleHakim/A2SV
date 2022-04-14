class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        maxOper = 0
        i = 0
        j = len(nums)-1
        while (i < j):
            if (nums[i] + nums[j] == k):
                maxOper +=1
                i +=1
                j -=1
            elif (nums[i] + nums[j] < k):
                i +=1
            else:
                j -=1
        return maxOper             
