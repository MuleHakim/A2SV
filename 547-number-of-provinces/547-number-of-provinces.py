class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num = 0
        def dfs(start):
            for k in range(len(isConnected[start])):
                if isConnected[start][k] == 1 and k not in visited:
                    visited.add(k)
                    dfs(k)
        for row in range(len(isConnected[0])):
            if isConnected[row][row] == 1 and row not in visited:
                visited.add(row)
                dfs(row)
                num += 1
        return num