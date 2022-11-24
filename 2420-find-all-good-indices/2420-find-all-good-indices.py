class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        res = []
        dec, inc = [1]*len(nums), [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                dec[i] = dec[i-1] + 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= nums[i+1]:
                inc[i] = inc[i+1] + 1

        for i in range(k,len(nums)-k):
            if dec[i-1] >= k and inc[i+1] >= k:
                res.append(i)
        return res