class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        res = 0
        arrow = -math.inf
        for point in points:
            if point[0] > arrow:
                res += 1
                arrow = point[1]
        return res