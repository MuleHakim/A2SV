"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        output = []
        low = 1
        high = 1000
        while 1 <= low <= 1000 and 1 <= high <= 1000:
            fun = customfunction.f(low, high)
            if fun == z:
                output.append([low, high])
                low += 1
            elif fun > z:
                high -= 1
            else:
                low += 1
        return output
