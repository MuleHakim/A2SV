class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s = nums[0]
        l = nums[-1]
        if s % l == 0:
            return l
        else:
            return gcd(l, s % l)