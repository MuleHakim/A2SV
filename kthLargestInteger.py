class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        
        def merge(nums):
            if len(nums) > 1:
                left_nums = nums[:len(nums)//2]
                right_nums = nums[len(nums)//2:]

                merge(left_nums)
                merge(right_nums)
                Merge(left_nums,right_nums,nums)
                return nums

        def Merge(left_nums,right_nums,nums):
                i = 0
                j = 0
                k = 0

                while i < len(left_nums) and j < len(right_nums):
                    if left_nums[i] < right_nums[j]:
                        nums[k] = left_nums[i]
                        i += 1
                    else:
                        nums[k] = right_nums[j]
                        j += 1
                    k += 1
                while i < len(left_nums):
                    nums[k] = left_nums[i]
                    i += 1
                    k += 1

                while j < len(right_nums):
                    nums[k] = right_nums[j]
                    j += 1
                    k += 1
        merge(nums)
        for i in nums:
            if i != 0:
                return str(nums.pop(-(k-1)-1))
        return str(nums.pop())
      
