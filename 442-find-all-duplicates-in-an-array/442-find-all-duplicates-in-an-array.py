class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        # nums.append(0)
        idx = len(nums)
        for i in counter.keys():
            if counter[i]==2:
                nums.append(i)
        return nums[idx:]