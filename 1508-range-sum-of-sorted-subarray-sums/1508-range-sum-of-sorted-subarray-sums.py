class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        tmp = [] + nums
        i = 0
        j = i+2
        while i!=len(nums)-1:
            tmp.append(sum(nums[i:j]))
            j += 1
            if j==len(nums)+1:
                i += 1
                j = i+2
        tmp.sort()
        return sum(tmp[left-1:right])%((10**9)+7)
        
    