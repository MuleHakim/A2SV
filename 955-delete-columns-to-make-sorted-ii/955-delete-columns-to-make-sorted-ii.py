class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        end = 0
        output = 0
        while end < len(strs[0]):
            for i in range(len(strs)-1):
                if strs[i][:end+1] > strs[i+1][:end+1]:
                    output += 1
                    for j in range(len(strs)):
                        strs[j] = strs[j][:end] + strs[j][end+1:]
                    end -= 1
                    break
                else:
                    continue
            end += 1
        return output