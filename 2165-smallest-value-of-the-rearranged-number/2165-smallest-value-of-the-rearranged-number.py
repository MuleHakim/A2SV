class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            num = sorted(str(num))
            temp = []
            for i in range(len(num)):
                if num[i]=="0":
                    temp.append(num[i])
                    
            for i in temp:
                num.insert(len(temp)+1,i)
            ans = "".join(num)
            ans = int(ans)
            return ans
            
                
        else:
            # num = num * (-1)
            # num = str(num)
            # num = num[::-1]
            # num = list(num)
            num = num * (-1)
            num = str(num)
            num = sorted(num,reverse=True)
            ans = "".join(num)
            answer = int(ans)
            return answer * (-1)