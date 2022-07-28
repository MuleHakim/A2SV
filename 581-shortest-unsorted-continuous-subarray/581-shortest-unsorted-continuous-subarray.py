class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return 0

        min_val = float('inf')
        max_val = float('-inf')

        found = False
        for i in range(len_nums-1):
            if nums[i] > nums[i+1]:
                found = True
            if found:
                min_val = min(min_val, nums[i+1])

        found = False
        for j in range(len_nums-1, -1, -1):
            if nums[j] < nums[j-1]:
                found = True
            if found:
                max_val = max(max_val, nums[j])

        for left in range(len_nums):
            if min_val < nums[left]:
                break

        for right in range(len_nums-1, -1, -1):
            if max_val > nums[right]:
                break

        if right - left < 0:
            return 0
        else:
            return right -left + 1