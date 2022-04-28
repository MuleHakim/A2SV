class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLength = 0
        maxHeap = []
        minHeap = []
        i = 0
        j = 0
        while (j < len(nums)):
            currEl = nums[j]
            while (len(maxHeap) > 0 and nums[maxHeap[-1]] <= currEl):
                del maxHeap[-1]
            maxHeap.append(j)
            while (len(minHeap) > 0 and nums[minHeap[-1]] >= currEl):
                del minHeap[-1]
            minHeap.append(j)
            maxOfSub = nums[maxHeap[0]]
            minOfSub = nums[minHeap[0]]
            if (maxOfSub - minOfSub <= limit):
                currLength = j - i + 1
                if (maxLength < currLength):
                    maxLength = currLength
            else:
                i += 1
                while (len(minHeap) > 0 and minHeap[0] < i):
                    del minHeap[0]

                while (len(maxHeap) > 0 and maxHeap[0] < i):
                    del maxHeap[0]

            j += 1
        return maxLength
