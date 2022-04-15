class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        for key,value in count.items():
            freq[value].append(key)

        output = []
        for i in range(len(freq)-1,0,-1):
            for value in freq[i]:
                output.append(value)
                if len(output)== k:
                    return output
