class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:                        
        queue = [start]
        visited = [False] * len(arr)
        while queue:
            n = queue.pop()
            if arr[n] == 0:
                return True
            visited[n] = True
            if n-arr[n] >= 0 and visited[n-arr[n]] == False:
                queue.append(n-arr[n])
            if n+arr[n] < len(arr) and visited[n+arr[n]] == False:
                queue.append(n+arr[n])
        return False
    
        # # Array
        # s = {start}
        # q = [start]
        # i in (tmp+arr[tmp], tmp-arr[tmp]):
        #         if 0 <= i < len(arr):
        #             if arr[i] == 0:
        #                 return True
        #             if i not in s:
        #                 q.append(i)
        #                 s.add(i)