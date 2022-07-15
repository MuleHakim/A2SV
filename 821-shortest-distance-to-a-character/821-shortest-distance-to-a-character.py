class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [ i for i in range(len(s)) if s[i]==c ]
        output = []
        p = 0
        for i in range(len(s)):
            if i < indices[0]:
                output.append(indices[0]-i)
            elif i > indices[-1]:
                output.append(i-indices[-1])
            elif i == indices[p]:
                output.append(0)
                p += 1
            else:
                output.append(min(indices[p]-i, i-indices[p-1]))
        return output