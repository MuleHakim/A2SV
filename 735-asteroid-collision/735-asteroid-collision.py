class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        for ast in asteroids:
            while output and ast < 0 < output[-1]:
                if output[-1] < abs(ast):
                    output.pop()
                    continue
                elif output[-1] == abs(ast):
                    output.pop()
                break
            else:
                output.append(ast)
        return output