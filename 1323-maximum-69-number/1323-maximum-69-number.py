class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = ""
        while True:
            eachNum = num%10
            num = num//10
            temp += str(eachNum)
            if num<10:
                temp += str(num)
                break
        temp = temp[::-1]
        temp = [ i for i in temp ]
        for i in range(len(temp)):
            if int(temp[i])==6:
                temp[i] = "9"
                return int("".join(temp))
        return int("".join(temp))