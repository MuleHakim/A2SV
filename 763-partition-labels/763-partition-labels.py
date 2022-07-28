class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx= { x: k  for k, x in enumerate(s)}
        output = []
        maxN = 0
        cumsum = 0
        for i, char in enumerate(s):
            maxN = max(last_idx[char], maxN)
            if maxN == i:
                di = i + 1 - cumsum
                cumsum += di
                output.append(di)
        return output