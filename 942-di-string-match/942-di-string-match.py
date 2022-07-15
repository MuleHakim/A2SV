class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        output = []
        mini = 0
        maxi = len(s)
        for i in s:
            if i == 'I':
                output.append(mini)
                mini += 1
            else:
                output.append(maxi)
                maxi -= 1
        output.append(mini)
        return output