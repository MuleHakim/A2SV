class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        totalF = 0
        totalS = 0
        for i in range(firstLen+secondLen):
            if i < firstLen:
                totalF += nums[i]
            else:
                totalS += nums[i]
        
        output1 = totalS + totalF
        maxF = totalF
        for i in range(firstLen+secondLen,len(nums)):
            totalS += nums[i] - nums[i - secondLen]
            totalF += nums[i - secondLen] - nums[i - firstLen - secondLen]
            maxF = max(maxF, totalF)
            output1 = max(output1, maxF + totalS)
        
        totalF = 0
        totalS = 0
        for i in range(firstLen+secondLen):
            if i < secondLen:
                totalF += nums[i]
            else:
                totalS += nums[i]
        
        output2 = totalS + totalF
        maxS = totalS
        for i in range(firstLen+secondLen,len(nums)):
            totalF += nums[i] - nums[i - firstLen]
            totalS += nums[i - firstLen] - nums[i - secondLen - firstLen]
            maxS = max(maxS, totalS)
            output2 = max(output2, maxS + totalF)
        return max(output1,output2)