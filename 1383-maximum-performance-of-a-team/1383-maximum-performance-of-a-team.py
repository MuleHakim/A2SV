class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = sorted([(s, e) for s, e in zip(speed, efficiency)], key=lambda x: x[1], reverse=True)
        speed_total = 0
        ans = 0
        speed_heap = []
        for s, e in arr:
            heapq.heappush(speed_heap, s)
            if len(speed_heap) > k:
                speed_total -= heapq.heappop(speed_heap)
            speed_total += s
            ans = max(ans, e * speed_total)
        return ans % (10 ** 9 + 7)