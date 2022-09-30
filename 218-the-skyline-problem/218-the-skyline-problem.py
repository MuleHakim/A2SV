class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        i, n = 0, len(buildings)
        live = []
        while i < n or live:
            if not live or i < n and buildings[i][0] <= -live[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(live, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -live[0][1]
                while live and -live[0][1] <= x:
                    heappop(live)
            height = len(live) and -live[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline