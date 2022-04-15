class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i  in range(len(l)):
            for i  in range(len(l)):
                output.append(self.checkArthimetic(nums[l[i]:r[i]+1]))
            return output
    
    def checkArthimetic(self,subArr):
        subArr = sorted(subArr)
        diff = subArr[1]-subArr[0]
        for j in range(len(subArr)-1):
            if(subArr[j+1]-subArr[j]!=diff):
                return False
        return True
    
    
