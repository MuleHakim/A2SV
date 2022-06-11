class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = len(s)
        countA = s.count("a")
        countB = 0
        for i in s:
            ans = min(ans,countB + countA)
            if i == "a":
                countA -= 1
            else:
                countB += 1
        ans = min(ans,countA + countB)
        return ans