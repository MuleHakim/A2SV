class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = dict(sorted(counter.items(), key=lambda x:x[1],reverse=True))
        res = ''
        for i,j in zip(counter.values(),counter.keys()):
            res += i*j
        return res