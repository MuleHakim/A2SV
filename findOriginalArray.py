class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        times = 0
        if len(changed) % 2 != 0:
            return []
        else:
            for i in range(len(changed)):
                if changed[i]==0:
                    times +=1
                else:
                    for j in range(len(changed)):
                        if changed[i]*2 == changed[j] and changed[i]!=0 and len(original)<(len(changed)//2):
                            original.append(changed[i])
                            break
            if times%2!=0:
                return []
            elif times%2==0:
                for i in range(times//2):
                    original.append(0)
            return original if len(original) == len(changed)//2 else []
          
