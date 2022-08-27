class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        tmp=[]
        F1=1
        F2=1
        tmp.append(F1)
        tmp.append(F2)
        output=[]
        while(F1+F2<=k):
            tmp.append(F1+F2)
            F1,F2=F2,F1+F2
        for i in range(len(tmp)-1,-1,-1):
            if(tmp[i]<k):
                k-=tmp[i]
                output.append(tmp[i])
            elif(tmp[i]==k):
                output.append(tmp[i])
                break
        return len(output)