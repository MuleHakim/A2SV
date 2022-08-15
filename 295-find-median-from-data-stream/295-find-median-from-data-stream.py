class MedianFinder:

    def __init__(self):
        self.upperHeap = [float('inf')]
        self.lowerHeap = [float('inf')]

    def addNum(self, num):
        upperMin = + self.upperHeap[0]
        lowerMax = - self.lowerHeap[0]

        if num > upperMin or (lowerMax<=num<=upperMin and len(self.upperHeap)==len(self.lowerHeap)):
            heappush(self.upperHeap, num)
        else:
            heappush(self.lowerHeap, -num)

        if len(self.upperHeap)-len(self.lowerHeap) > 1:
            heappush( self.lowerHeap, -heappop( self.upperHeap ) )
        elif len(self.lowerHeap) > len(self.upperHeap):
            heappush( self.upperHeap, -heappop( self.lowerHeap ) )


    def findMedian(self):
        if len(self.upperHeap) == len(self.lowerHeap):
            upperMin = + self.upperHeap[0]
            lowerMax = - self.lowerHeap[0]
            return ( float(upperMin) + float(lowerMax) ) / 2.0
        else:
            assert len(self.upperHeap) == len(self.lowerHeap) + 1
            return float(self.upperHeap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()