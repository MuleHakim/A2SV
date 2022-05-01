class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]==0:
                nums.append(nums.pop(i))
                j -= 1
            else:
                i += 1

        return nums
