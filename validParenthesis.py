class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"(":")","[":"]","{":"}"}
        listOfKeys = [key for key in dict.keys()]
        listOfValues = [value for value in dict.values()]
        temp = []
        for i in s:
            if i in listOfKeys:
                temp.append(i)
            elif i == listOfValues[0] and len(temp) != 0 and temp[-1] == listOfKeys[0]:
                temp.pop()
            elif i == listOfValues[1] and len(temp) != 0 and temp[-1] == listOfKeys[1]:
                temp.pop()
            elif i == listOfValues[2] and len(temp) != 0 and temp[-1] == listOfKeys[2]:
                temp.pop()
            else:
                return False
        return temp==[]
 
