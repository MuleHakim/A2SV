class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        dict_ = {word[::-1]: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            if "" in dict_ and dict_[""] != i and word == word[::-1]:
                ans.append([i, dict_[""]])
            for j in range(1, len(word)+1):
                l = word[:j]
                r = word[j:]
                if l in dict_ and dict_[l] != i and r == r[::-1]:
                    ans.append([i, dict_[l]])
                if r in dict_ and dict_[r] != i and l == l[::-1]:
                    ans.append([dict_[r], i])
        return ans