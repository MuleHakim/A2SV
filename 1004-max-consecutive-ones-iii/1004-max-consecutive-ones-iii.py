class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            if k < 0:
                if nums[left]==0:
                    k += 1
                left += 1
        return i-left+1