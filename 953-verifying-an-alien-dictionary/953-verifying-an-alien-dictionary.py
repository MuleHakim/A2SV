class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}
        for index, val in enumerate(order):
            dict[val] = index
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if dict[words[i][j]] > dict[words[i+1][j]]:
                        return False
                    break
        return True