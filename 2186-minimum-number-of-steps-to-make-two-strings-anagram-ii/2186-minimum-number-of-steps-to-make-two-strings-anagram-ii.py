class Solution:
    def minSteps(self, s: str, t: str) -> int:
        output = 0
        s = collections.Counter(s)
        t = collections.Counter(t)
        for i in s.keys():
            if i not in t:
                output += s[i]
            else:
                output += abs(s[i]-t[i])
        for i in t.keys():
            if i not in s:
                output += t[i]
        return output