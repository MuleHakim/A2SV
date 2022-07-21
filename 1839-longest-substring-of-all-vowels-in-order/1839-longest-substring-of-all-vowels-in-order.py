class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        output = 0
        count = 1
        l = 0
        for r in range(1, len(word)):
            curr = word[r]
            prev = word[r - 1]
            if curr >= prev:
                if curr > prev:
                    count += 1
                if count == 5:
                    output = max(output, r - l + 1)
            else:
                count = 1
                l = r
        return output

        # output = ""
        # i = 0
        # k = i + 2
        # while i<len(word)-1:
        #     temp = word[i:k]
        #     tempSorted = "".join(sorted(temp))
        #     if temp==tempSorted:
        #         k += 1
        #         if len(set(temp))==5 and len(temp) > len(output):
        #             output = temp
        #         if k>len(word):
        #             break
        #     else:
        #         i = k - 1
        #         k = i + 2
        # return len(output)