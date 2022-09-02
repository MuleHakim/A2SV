class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x: x[0])
        output = 0
        for i in range(len(points)-1):
            output = max(output,points[i+1][0]-points[i][0])
        return output