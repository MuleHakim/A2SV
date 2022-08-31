class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:        
        answer = [[],[]]
        lose_dict = collections.defaultdict(int)
        all_players = set()
        for match in matches:
            winner = match[0]
            loser = match[1]
            lose_dict[loser] += 1
            all_players.add(winner)
            all_players.add(loser)
            
        for p in all_players:
            if p not in lose_dict:
                answer[0].append(p)
            elif lose_dict[p] == 1:
                answer[1].append(p)
        answer[0].sort()
        answer[1].sort()
        return answer