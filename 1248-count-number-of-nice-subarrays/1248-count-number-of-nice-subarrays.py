class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = collections.defaultdict(int)
        total = 0
        output = 0
        prefix[0] = 1
        for i in range(len(nums)):
            total += nums[i] & 1
            output += prefix[total-k]
            prefix[total] += 1
        return output
        # string = [ "0" if i%2==0 else "1" for i in nums]
        # string = "".join(string)
        # output = 0
        # for i in range(len(string)):
        #     if i==0:
        #         if string[i:-1].count("1")==k:
        #             output += 1
        #     else:
        #         if string[i:].count("1")==k:
        #             output += 1
        # return output