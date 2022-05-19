class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(1,len(gain)):
            gain[i] = gain[i-1] + gain[i]
        tempMax = max(gain)
        if tempMax>0:
            return tempMax
        return 0