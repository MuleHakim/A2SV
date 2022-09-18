class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start==goal:
            return 0
        res = 0
        b_start = bin(start)[2:]
        b_goal = bin(goal)[2:]
        if len(b_start)>len(b_goal):
            b_goal = (len(b_start)-len(b_goal))*"0" + b_goal
        elif len(b_start)<len(b_goal):
            b_start = (len(b_goal)-len(b_start))*"0" + b_start
        for i in range(len(b_start)-1,-1,-1):
            if b_goal[i]!=b_start[i]:
                res += 1
        return res