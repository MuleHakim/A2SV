class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, low, high):
            i = low + 1
            j = high 
            while True:
                while i <= j and nums[i] <= nums[low]: i+= 1
                while j >= i and nums[j] >= nums[low]: j-= 1
                if i > j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[low], nums[j] = nums[j], nums[low]
            return j
        k = len(nums) - k
        low = 0
        high = len(nums)-1
        while low < high:
            i = quickselect(nums, low, high)
            if i < k:
                low = i + 1
            elif i > k:
                high = i - 1
            else:
                break
        return nums[k]
