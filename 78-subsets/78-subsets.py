class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(nums, start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums,i+1,path)
                path.pop()
        backtrack(nums, 0, [])
        return result