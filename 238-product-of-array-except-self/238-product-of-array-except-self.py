class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     output.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
        # return output
        
        output = [1 for i in range(len(nums))]
        for i in range(1,len(output)):
            output[i] = output[i-1]*nums[i-1]
        rightPro = 1
        for i in range(len(output)-1, -1, -1):
            output[i] = output[i]*rightPro
            rightPro *= nums[i]
        return output