class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for l, r in ranges:
            if l <= left <= r:
                left = r+1
        return left > right