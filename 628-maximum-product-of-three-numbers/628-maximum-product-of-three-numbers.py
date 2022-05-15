class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # output = 0
        i = 0
        j = len(nums)-1
        max_right = max((nums[j]*nums[j-1]*nums[j-2]),(nums[i]*nums[j]*nums[j-1]))
        max_left = max((nums[i]*nums[i+1]*nums[i+2]),nums[i]*nums[i+1]*nums[j])
        return max(max_right,max_left)
        # if len(nums)==3:
        #     output += nums[i]*nums[i+1]*nums[j]
        # elif len(nums)==4:
        #     if nums[i]*nums[i+1] > nums[j]*nums[j-1]:
        #         output += nums[i]*nums[i+1]*nums[i+2]
        #     else:
        #         output += nums[j]*nums[j-1]*nums[j-2]
        # else:
        #     if nums[i]*nums[i+1] > nums[j]*nums[j-1]:
        #         if nums[j]<=0:
        #             output = nums[j]*nums[j-1]*nums[j-2]
        #         else:
        #             output = nums[i]*nums[i+1]*nums[j]
        #     else:
        #         if nums[j-3]<=0:
        #             output = nums[i]*nums[i+1]*nums[j]
        #         else:
        #             output = nums[j]*nums[j-1]*nums[j-2]
           
        # return output