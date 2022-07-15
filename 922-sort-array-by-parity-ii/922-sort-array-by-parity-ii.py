class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, key=lambda x: x%2)
        i = 0
        j = len(nums)-2
        while i<j:
            nums.insert(i+1,nums.pop())
            i += 2
        return nums