class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tmp = []
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            if tmp in grid:
                output += grid.count(tmp)
            tmp.clear()
        return output