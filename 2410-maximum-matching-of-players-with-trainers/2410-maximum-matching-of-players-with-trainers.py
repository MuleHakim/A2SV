class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players.sort()
        trainers.sort()
        for i, trainer in enumerate(trainers):
            if players[res] <= trainers[i]:
                res += 1
                if res == len(players):
                    return res
        return res