class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score_1 = 0
        score_2 = 0
        for i in range(len(nums)):
            score_2 += nums[i]
        score_1 = self.check(nums,0,len(nums)-1,1)
        score_2 -= score_1

        return score_1 >= score_2

    def check(self,nums,i,j,player):
        if i>j:
            return 0
        if player==1:
            return max(nums[i] + self.check(nums,i+1,j,2),nums[j] + self.check(nums,i,j-1,2))
        else:
            return min(self.check(nums,i+1,j,1), self.check(nums,i,j-1,1))
        
