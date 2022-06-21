class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        output = 0
        count = collections.defaultdict(int)
        for j, v in enumerate(fruits):
            count[v] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            output = max(output, j-i+1)
        return output