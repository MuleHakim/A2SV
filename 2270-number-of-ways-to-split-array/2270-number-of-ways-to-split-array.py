class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # output = 0
        # for i in range(len(nums)-1):
        #     if sum(nums[:i+1])>=sum(nums[i+1:]):
        #         output += 1
        # return output
        
        pre = 0
        suf = sum(nums)
        output = 0
        for i in range(len(nums)-1):
            pre += nums[i]
            suf -= nums[i]
            if pre >= suf:
                output += 1
        return output