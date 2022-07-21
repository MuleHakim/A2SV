class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(list(str(num)))
        return int(num[0]+num[-1]) + int(num[1]+num[2])