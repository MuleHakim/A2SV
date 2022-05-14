class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] != target:
                j -= 1
                if j==i:
                    j = len(nums)-1
                    i += 1
            else:
                output.append(i)
                output.append(j)
                return output