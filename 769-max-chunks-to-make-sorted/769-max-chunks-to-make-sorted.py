class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, maxValue = 0, -1
        for i, v in enumerate(arr):
            maxValue = max(maxValue, v)
            if maxValue == i:
                res += 1
        return res