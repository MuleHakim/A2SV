class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        low = 0
        high = len(grid[0])-1
        output = 0
        while low<len(grid) and high>=0:
            if grid[low][high]<0:
                output += len(grid)-low
                high = high-1
            else:
                low = low+1
        return output
