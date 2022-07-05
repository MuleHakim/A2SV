class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        output = ""
        for i in range(len(s)):            
            for j in range(len(s), 0, -1):
                substring = s[i:j]
                lower = set(substring.lower())
                mixed = set(substring)
                if len(mixed) == 2 * len(lower):
                    if len(substring) > len(output):
                        output = substring            
        return output