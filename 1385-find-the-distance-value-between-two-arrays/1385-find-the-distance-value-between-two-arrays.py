class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        output = 0
        for i in arr1:
            temp = False
            for j in arr2:
                if abs(i - j) <= d:
                    temp = True
            else:
                if temp==True:
                    output += 0
                else:
                    output += 1
        return output
    