class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in piles:
            heapq.heappush(heap,-i)
        for i in range(k):
            popped = heapq.heappop(heap)
            tmp = popped + math.floor(-popped/2)
            heapq.heappush(heap,tmp)
        return -sum(heap)