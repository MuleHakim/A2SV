class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        queue = deque()
        changed = sorted(changed)
        for num in changed:
            if queue and num == queue[0]:
                queue.popleft()
            else:
                queue.append(num*2)
                res.append(num)
        if queue:
            return [] 
        else:
            return res