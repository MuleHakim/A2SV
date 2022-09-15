class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dict = {}
        def totalPath(triangle, i, j):
            if i == len(triangle):
                return 0
            if (i, j) in dict:
                return dict[(i, j)]
            dict[(i, j)] = min(totalPath(triangle, i+1, j), totalPath(triangle, i+1, j+1)) + triangle[i][j]
            return min(totalPath(triangle, i+1, j), totalPath(triangle, i+1, j+1)) + triangle[i][j]
        return totalPath(triangle, 0, 0)
