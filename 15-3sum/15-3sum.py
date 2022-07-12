class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        i = 0
        while i<len(nums)-2:
            if i == 0 or nums[i] != nums[i-1]:
                j = i+1
                k = len(nums)-1
                while j<k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        output.append([nums[i], nums[j], nums[k]])
                        j = j+1
                        k = k-1
                        while j<k and nums[j] == nums[j-1]:
                            j += 1
                        while j<k and nums[k] == nums[k+1]:
                            k -= 1
            i += 1
        return output