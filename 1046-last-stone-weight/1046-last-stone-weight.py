class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for s in stones:
            heapq.heappush(heap,-s)
        while len(heap)>=2:
            i = heapq.heappop(heap)
            j = heapq.heappop(heap)
            if i!=j:
                heapq.heappush(heap,(i-j))
        return -heap[-1] if heap else 0