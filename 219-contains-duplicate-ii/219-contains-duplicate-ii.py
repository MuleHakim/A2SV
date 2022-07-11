class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        for i in range(len(nums)):
            if nums[i] in myDict:
                prev_index = myDict[nums[i]]
                if i - prev_index <= k:
                    return True
            myDict[nums[i]] = i
        return False