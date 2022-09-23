class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for i, num in enumerate(nums):
            if not stack or num<=nums[stack[-1]]:
                stack.append(i)
        for i, num in reversed(list(enumerate(nums))):
            while stack and num>=nums[stack[-1]]:
                res = max(res, i-stack.pop())
        return res