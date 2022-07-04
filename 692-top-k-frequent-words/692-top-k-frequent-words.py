class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        myDict = {}
        output = []
        words = sorted(words)
        for word in words:
            if word not in myDict:
                myDict[word] = 1
            else:
                myDict[word] += 1
        myDict = dict(sorted(myDict.items(), reverse=True, key=lambda x: x[1]))
        for word in myDict.keys():
            if len(output) != k:
                output.append(word)
        return output