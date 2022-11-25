class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []
        
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                
                count = (mid - left) * (right - mid)
                res += (arr[mid] * count)
                
            stack.append(i)
                
        return res % (10**9 + 7)