class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        output = 0
        i = 0
        for h in houses:
            while (i+1 < len(heaters) and h-heaters[i] > heaters[i+1]-h):
                i += 1
            output = max(output, abs(heaters[i]-h))
        return output