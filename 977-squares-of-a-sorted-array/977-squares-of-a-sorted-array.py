class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            a = nums.pop(0)
            nums.append(a*a)
        nums = sorted(nums)
        return nums