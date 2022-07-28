class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right = 0
        for ch in s:
            if ch == '[':
                left += 1
            else:
                left -= 1
            if left < 0:
                left = 0
                right += 1
        return (right + 1) // 2