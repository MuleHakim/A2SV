class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        minDiff = inf
        pre = 0
        suf = sum(nums)
        output = 0
        for i in range(len(nums)):
            pre += nums[i]
            suf -= nums[i]
            if i==len(nums)-1:
                diff = abs(pre//(i+1) - 0)
            else:
                diff = abs(pre//(i+1) - suf//(len(nums)-i-1))
            if diff < minDiff:
                output = i
                minDiff = diff
        return output