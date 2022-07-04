class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        while len(matrix)!=1:
            matrix[0] = matrix[0] + matrix[1]
            matrix.pop(1)
        for i in matrix[0]:
            matrix.append(i)
        matrix.remove(matrix[0])
        matrix = sorted(matrix)
        return matrix[k-1]
