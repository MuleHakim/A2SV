class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        output = 0
        totalDiff = 0
        tmpTotal = 0
        for i in range(len(gas)):
            totalDiff += gas[i]-cost[i]
            tmpTotal += gas[i]-cost[i]
            if tmpTotal < 0:
                tmpTotal = 0
                output = i + 1
        if totalDiff < 0:
            return -1
        else:
            return output
        
        # for i in range(len(gas)):
        #     if gas[i]>=cost[i]:
        #         circularGas = gas[i:] + gas[:i+1]
        #         circularCost = cost[i:] + cost[:i+1]
        #         tmp1 = circularGas[0]
        #         tmp2 = circularCost[0]
        #         for j in range(1,len(circularGas)):
        #             tmp1 += circularGas[j]
        #             tmp2 += circularCost[j]
        #             if tmp1<tmp2:
        #                 break
        #         else:
        #             return i