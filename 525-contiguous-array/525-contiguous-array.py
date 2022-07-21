class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        dic = {0:-1}
        total = 0
        output = 0
        for i in range(len(nums)):
            total = total+nums[i]
            if total in dic.keys():
                output = max(output, i-dic[total])
            else:
                dic[total] = i
        return output