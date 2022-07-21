class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            if len(str(i))%2==0:
                output += 1
        return output