class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x:(-x[0],x[1]))
        count = 0
        max_d = 0
        for i in range(len(properties)) : 
            if properties[i][1] < max_d : 
                count +=  1 
            else : 
                max_d = properties[i][1]
        return count