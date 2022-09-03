class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        for i in counter.keys():
            if counter[i]==1:
                tmp = nums.pop(nums.index(i))
                nums.append(tmp)
        return nums[len(nums)-2:]