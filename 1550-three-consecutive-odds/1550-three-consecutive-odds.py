class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        k = 3
        while i<len(arr)-2:
            for j in arr[i:i+k]:
                if j%2==0:
                    break
            else:
                return True
            i += 1
        return False