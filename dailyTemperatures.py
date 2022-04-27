class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
            if not T:
                return []
            output = [0] * len(T)
            stack = []
            for i, v in enumerate(T):
                while stack and stack[-1][0] < v:
                    topIndex = stack.pop()[1]
                    count = i - topIndex
                    output[topIndex]=count
                stack.append((v, i))
            return output
