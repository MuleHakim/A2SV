class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        total = 0
        hash = defaultdict(lambda: 0)
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                output += 1
            if total-k in hash:
                output += hash[total-k]
            hash[total] += 1
            
            
#         output = 0
#         for i in range(len(nums)):
#             total = 0           
#             for j in range(i,len(nums)):
#                 total += nums[j]
#                 if total == k:
#                     output += 1
        return output
    
