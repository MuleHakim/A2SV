class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = floor(sqrt(c))
        sqrA = a*a
        sqrB = b*b
        while(sqrA<=sqrB):
            if sqrA+sqrB == c:
                return True
            if sqrA+sqrB > c:
                b -= 1
            if sqrA+sqrB < c:
                a += 1
            sqrA = a*a
            sqrB = b*b
        return False
    
        # sqr = []
        # for i in range(c+1):    # 0 1 2 3 4  5
        #     if (i*i)>c:         # 0 1 4 9 16 25
        #         break
        #     if (i*i)<=c:
        #         sqr.append(i*i)
        # i = 0
        # j = len(sqr)-1
        # while i<j:
        #     if c==sqr[i]:
        #         return True
        #     if sqr[i]+sqr[i+1]==c:
        #         return True
        #     if sqr[i]+sqr[i+1]<c:
        #         i += 1
        #     elif sqr[i]+sqr[i+1]<c:
        #         j -= 1
        # return False