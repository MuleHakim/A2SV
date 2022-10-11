class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        total = 0
        for i in sorted(costs):
            total += i
            res += 1
            if total>coins:
                return res-1
        return len(costs)