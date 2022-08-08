class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            day = 1
            wt = 0
            mid = (low + high) //2
            for weight in weights:
                if wt + weight > mid:
                    day += 1
                    wt = 0
                wt += weight
            if day <= days:
                high = mid
            else:
                low = mid + 1
        return low