class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        n_list = [ i for i in range(1,n+1) ]
        output = []
        i = 0
        while i<len(n_list) and target:
            if n_list[i] in target:
                output.append("Push")
                target.pop(0)
            else:
                output.append("Push")
                output.append("Pop")
            i += 1
        return output