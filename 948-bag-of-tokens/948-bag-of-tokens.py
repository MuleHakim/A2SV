class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        output = 0
        score = 0
        while r >= l:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                output = max(output, score)
            elif power < tokens[l] and score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                return output
        return output