class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        i = 0
        j = len(nums)-1
        while i<=j:
            if nums[i]+nums[j] <= target:
                res += pow(2,j-i,(10**9 + 7))
                i += 1
            else:
                j -= 1
        return res % (10**9 + 7)