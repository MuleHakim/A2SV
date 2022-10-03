class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        sum_time,max_time = 0,0
        for i in range(len(colors)):
            if i>0 and colors[i-1] != colors[i]:
                total_time += sum_time - max_time
                sum_time = 0
                max_time = 0
            sum_time += neededTime[i]
            max_time = max(max_time, neededTime[i])
        total_time += sum_time - max_time
        return total_time