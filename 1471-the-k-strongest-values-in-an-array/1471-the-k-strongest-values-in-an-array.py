class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        if len(arr)==1:
            return arr
        median = (len(arr)-1)//2
        i = 0
        j = len(arr)-1
        output = []
        while len(output)!=k:
            if arr[j]-arr[median] > arr[median]-arr[i]:
                output.append(arr[j])
                j -= 1
            elif arr[median]-arr[i] > arr[j]-arr[median]:
                output.append(arr[i])
                i += 1
            else:
                if arr[i]>arr[j]:
                    output.append(arr[i])
                    i += 1
                else:
                    output.append(arr[j])
                    j -= 1
        return output