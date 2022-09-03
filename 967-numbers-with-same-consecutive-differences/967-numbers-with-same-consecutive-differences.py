class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        dp = set(range(10))
        for i in range(1, n):
            prev_dp = dp
            dp = set()
            for num in prev_dp:
                if num == 0:
                    continue
                left = num % 10
                if left >= k:
                    dp.add(num*10+left-k)
                if left + k <= 9:
                    dp.add(num*10+left+k)
        return sorted(list(dp))