class Solution:
    def minSteps(self, s: str, t: str) -> int:
        output = 0
        s = collections.Counter(s)
        t = collections.Counter(t)
        for i in s.keys():
            if i not in t:
                output += s[i]
            elif i in t and s[i]>t[i]:
                output += s[i]-t[i]
        return output
