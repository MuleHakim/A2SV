class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            counter = defaultdict(int)
            i = res = 0
            for j,num in enumerate(nums):
                counter[num] += 1
                while len(counter) > k:
                    counter[nums[i]] -= 1
                    if counter[nums[i]] == 0:
                        del counter[nums[i]]
                    i += 1
                res += j-i+1
            return res
        return atMostK(k)-atMostK(k-1)
    
        # if k==1 and len(nums)==len(set(nums)): return len(nums)
        # if k>len(nums): return 0
        # if k==len(nums) and k>len(set(nums)): return 0
        # i = 0
        # j = i + k
        # result = 0
        # while not j==len(nums) and not (j-i<k):
        #     tmp = nums[i:j]
        #     count = len(set(tmp))
        #     if count<k:
        #         if j==len(nums): i += 1
        #         else: j += 1
        #     elif count==k:
        #         if j==len(nums) and j-i>k:
        #             i += 1
        #             j = i + k
        #         elif j==len(nums): i += 1
        #         else: j += 1
        #         result += 1
        #     else:
        #         i += 1
        #         j = i + k
        # return result