class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(pos):
            if pos==len(nums)-1:
                output.append(nums[:])
            for i in range(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos+1)
                nums[pos], nums[i] = nums[i], nums[pos]
        dfs(0)
        return output