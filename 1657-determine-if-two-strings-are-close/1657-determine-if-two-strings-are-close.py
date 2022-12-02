class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = list(word1)
        word2 = list(word2)
        word1.sort()
        word2.sort()
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        if len(word1)!=len(word2): return False
        if word1==word2: return True
        counter1, counter2 = Counter(word1), Counter(word2)
        return sorted(counter1.values())==sorted(counter2.values()) and set(counter1.keys())==set(counter2.keys())