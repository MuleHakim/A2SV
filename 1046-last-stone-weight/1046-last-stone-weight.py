class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                x = stones.pop(-2)
                y = stones.pop(-1)
                stones.append(y-x)
            if len(stones)<=1:
                break
        return stones[-1] if stones else 0