class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = collections.Counter({0: 1})
        prevTotal = output = 0
        for i in nums:
            prevTotal += i
            output += c[prevTotal - goal]
            c[prevTotal] += 1
        return output