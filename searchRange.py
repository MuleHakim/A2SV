class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target + 1)
        if l == len(nums) or l >= r:
            return [-1, -1]
        return [l, r - 1]
