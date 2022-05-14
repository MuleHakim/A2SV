class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        maxSum = total
        for i in range(1,len(nums)-k+1):
            total -= nums[i-1]
            total += nums[k+i-1]
            maxSum = max(maxSum,total)
        return maxSum/k