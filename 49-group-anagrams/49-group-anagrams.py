class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = collections.defaultdict(list)
        output = []
        for s in strs:
            sorted_str = ("").join(sorted(s))
            myDict[sorted_str].append(s)
        for v in myDict.values():
            v.sort()
            output.append(v)
        return output