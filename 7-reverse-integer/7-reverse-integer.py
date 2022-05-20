class Solution:
    def reverse(self, x: int) -> int:
        temp = ""
        if x>0:
            while True:
                if x<10:
                    temp += str(x)
                    break
                eachNum = x%10
                x = x//10
                temp += str(eachNum)
                if x<10:
                    temp += str(x)
                    break
            num = int(temp)
            if num>(pow(2,31)-1):
                return 0
            return num
        elif x==0:
            return 0
        else:
            x = x*(-1)
            while True:
                if x<10:
                    temp += str(x)
                    break
                eachNum = x%10
                x = x//10
                temp += str(eachNum)
                if x<10:
                    temp += str(x)
                    break
            num = int(temp)*(-1)
            if num<(pow(2,31)*(-1)):
                return 0
            return num