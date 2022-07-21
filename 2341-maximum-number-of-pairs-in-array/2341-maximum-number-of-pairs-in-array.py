class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        output = []
        nums = sorted(nums)
        i = 0
        pair = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
                nums.pop(i)
                pair += 1
            else:
                i += 1
        output.append(pair)
        output.append(len(nums))
        return output