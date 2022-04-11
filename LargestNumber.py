class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr = [str(num) for num in nums]
        def bubSort(numstr):
            for i in range(len(numstr)):
                for j in range(len(numstr)-1-i):
                    if numstr[j+1] < numstr[j]:
                        numstr[j+1],numstr[j] = numstr[j],numstr[j+1]
                        
        curr = [numstr[0]]
        for i in range(1, len(nums)):
            if curr[-1] + numstr[i] > numstr[i]+curr[-1]:
                numstr[i-len(curr)] = numstr[i]
                numstr[i] = curr[-1]
            elif curr[-1] + numstr[i] == numstr[i]+curr[-1]:
                curr.append(numstr[i])
            else:
                curr = [numstr[i]]
        
        result = ''.join(reversed(numstr)) 
        if int(result)>0:
            return result
        else:
            return '0'
        
