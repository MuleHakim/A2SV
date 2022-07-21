class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num_rev = int(str(int(str(num)[::-1]))[::-1])
        if num == num_rev:
            return True
        return False