class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_ = sum(i for i in nums if i%2==0)
        for i,j in queries:
            if nums[j]%2==0:
                sum_ -= nums[j]
            nums[j] += i
            if nums[j] % 2 == 0:
                sum_ += nums[j]
            res.append(sum_)
        return res