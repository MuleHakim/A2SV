class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = 0
        for i in accounts:
            output = max(output,sum(i))
        return output