class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = sum(arr)
        i = 0
        j = len(arr)-1
        while i<j:
            if len(arr[i:j+1])%2!=0:
                total += sum(arr[i:j+1])
                j -= 2
            else:
                j -= 1
            if i==j:
                i += 1
                j = len(arr)-1
            if j-i==1:
                break
        return total