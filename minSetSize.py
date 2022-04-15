class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        removed  = 0
        output = 0
        for key,value in sorted(counter.items(),key=lambda x: -x[1]):
            removed +=value
            output +=1
            if removed>=(len(arr)/2):
                break
        return output 
        
