class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        j = len(arr)-1
        while (j-i+1 > k):
            r = arr[j] - x
            l = x - arr[i]
            if r >= l:
                j -= 1
            else:
                i += 1
        return arr[i:j+1]