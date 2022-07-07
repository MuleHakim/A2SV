class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        decreasing = [0] * n
        increasing = decreasing.copy()
        output = []
        for i in range(1, n):
            if security[i] <= security[i-1]:
                decreasing[i] = decreasing[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                increasing[n-i-1] = increasing[n-i] + 1
        print(decreasing, increasing)
        for i in range(time, n-time):  
            if decreasing[i] >= time and increasing[i] >= time:
                output.append(i)  
        return output