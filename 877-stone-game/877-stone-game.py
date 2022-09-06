class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        tmp = {} 
        for i in range(len(piles)-1, -1, -1):
            for j in range(i, len(piles)):
                if i == j:
                    tmp[i] = piles[i]
                    previous = piles[i]
                else:
                    left = piles[i] + tmp[i+1]
                    right = piles[j] + previous
                    previous = max(left, right)
                    tmp[i] = max(left, right)
        return tmp[0] > 0