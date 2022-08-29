class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tmp = []
        for i in bills:
            if i==5:
                tmp.append(i)
            elif i==10 and 5 not in tmp:
                return False
            elif i==10 and 5 in tmp:
                tmp.remove(5)
                tmp.append(i)
            elif i==20 and 5 not in tmp:
                return False
            elif i==20 and 10 in tmp and 5 in tmp:
                tmp.remove(5)
                tmp.remove(10)
                tmp.append(i)
            elif i==20 and 10 not in tmp and tmp.count(5)>=3:
                tmp.remove(5)
                tmp.remove(5)
                tmp.remove(5)
                tmp.append(i)
            elif i==20 and 10 not in tmp and tmp.count(5)<3:
                return False
        return True