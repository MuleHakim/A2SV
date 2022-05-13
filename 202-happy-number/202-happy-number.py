class Solution:
    def isHappy(self, n: int) -> bool:
        dict = {}
        while n != 1 and n not in dict:
            dict[n] = True
            n = self.nextNumber(n)
        return n == 1

    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new += int(char)**2
        return new