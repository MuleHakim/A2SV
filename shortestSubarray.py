class Solution:
    def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        output, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                output = min(output, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        if output < float('inf'):
            return output 
        else:
            return -1
