class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        islands = 0
        neighbors = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands += 1
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        neighbors += 1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        neighbors += 1
        return islands * 4 - neighbors * 2