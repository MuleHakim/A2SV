class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        temp = []
        zero24 = False
        for i in timePoints:
            if int(i[:2])==0:
                zero24 = True
                temp.append(int(i[len(i)-2:]))
                temp.append(1440 + int(i[len(i)-2:]))
            else:
                temp.append(int(i[:2])*60 + int(i[len(i)-2:]))
                
        temp.sort()
        output = 1440
        for i in range(1,len(temp)):
            output = min(output,temp[i]-temp[i-1])
        if zero24:
            return output
        return min(output,1440-temp[-1]+temp[0])
    
        # temp = {}
        # for i in timePoints:
        #     if int(i[len(i)-2:])==0:
        #         if int(i[:2])==0:
        #             temp[24]=60
        #         else:
        #             temp[int(i[:2])]=60
        #     else:
        #         if int(i[:2])==0:
        #             temp[24]=int(i[len(i)-2:])
        #         else:
        #             temp[int(i[:2])]=int(i[len(i)-2:])
        # sort_temp = sorted(temp.items(), key=lambda x: x[0])
        # output = sort_temp[len(sort_temp)-1][1]-sort_temp[0][1]
        # for i in range(1,len(sort_temp)):
        #     output = min(output,sort_temp[i][1]-sort_temp[i-1][1])
        # return output