class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        licensePlate = ''.join([i for i in licensePlate if not i.isdigit()])
        licensePlate = licensePlate.replace(" ","")
        counter = collections.Counter(licensePlate)
        words = sorted(words,key=len)
        for word in words:
            for k, v in counter.items():
                if k not in word or word.count(k) < v:
                    break
            else:
                return word