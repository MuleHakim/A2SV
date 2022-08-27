class Solution:
    def minTimeToType(self, word: str) -> int:
        output = 0
        for i in range(len(word)):
            if i == 0 and word[i]=="a":
                output += 1
                continue
            if i == 0 and word[i] !="a":
                tmp = ord(word[i])-ord("a")
                if tmp >= 13:
                    output += (26-tmp) + 1
                else:
                    output += (tmp + 1)
                continue
            tmp = abs(ord(word[i])-ord(word[i-1]))
            if tmp >= 13:
                output += (26-tmp) + 1
            else:
                output += (tmp + 1)
        return output