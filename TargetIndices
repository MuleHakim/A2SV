class Solution:
    def targetIndices(nums, target: int):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    
        output = []
        for j in range(len(nums)):
            if nums[j] == target:
                output.append(j)

        return output
