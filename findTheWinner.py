class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nlist = deque(range(1,n+1))
        if len(nlist)==1:
            return nlist[0]
        while len(nlist) > 1:
            nlist.rotate(1-k)
            nlist.popleft()
        return nlist[0]
