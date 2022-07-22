class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output  = [-1]*len(score)
        sorted_score = sorted(score,reverse=True)
        for i in range(len(sorted_score)):
            if i==0:
                output[score.index(sorted_score[i])] = "Gold Medal"
            elif i==1:
                output[score.index(sorted_score[i])] = "Silver Medal"
            elif i==2:
                output[score.index(sorted_score[i])] = "Bronze Medal"
            else:
                output[score.index(sorted_score[i])] = str(i+1)
        return output