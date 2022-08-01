class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        toAdd = bal = 0
        for p in s:
            if p == "(":
                bal +=1
            elif p == ")" and bal > 0:
                bal-=1
            elif p == ")" and bal <= 0:
                toAdd +=1
        return bal + toAdd