class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output = 0
        for i in zip(*strs):
            a = sorted(i)
            i = list(i)
            if i!= a:
                output += 1
        return output
