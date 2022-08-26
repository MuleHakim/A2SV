class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R , D = True, True
        flag = 0
        senate = list(senate)
        while R and D:
            R, D = False, False
            for i in range(len(senate)) :
                if senate[i] == 'R' :
                    if flag < 0:
                        senate[i] = '0'
                    else:
                        R = True
                    flag += 1
                if senate[i] == 'D':
                    if flag > 0:
                        senate[i] = '0'
                    else:
                        D = True
                    flag -= 1
        if R:
            return "Radiant"
        else:
            return "Dire"