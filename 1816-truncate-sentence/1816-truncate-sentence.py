class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s = s[:k]
        return " ".join(s)