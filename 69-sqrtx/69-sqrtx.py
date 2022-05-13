class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        if x <= 1 :
            return x
        while(left < right-1):
            mid = left +  (right - left) // 2
            if mid == x // mid:
                return mid
            elif x//mid < mid:
                right = mid
            else:
                left = mid
        return left