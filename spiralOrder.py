class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
          
        totalItems = len(matrix) * len(matrix[0])
        output = []
        r1 = 0
        c1 = 0
        r2 = len(matrix) - 1
        c2 = len(matrix[0]) - 1

        while len(output) < totalItems:
            j = c1
            while j <= c2 and len(output) < totalItems:
                output.append(matrix[r1][j])
                j += 1
            i = r1 + 1
            while i <= r2 - 1 and len(output) < totalItems:
                output.append(matrix[i][c2])
                i += 1
            j = c2
            while j >= c1 and len(output) < totalItems:
                output.append(matrix[r2][j])
                j -= 1
            i = r2 - 1
            while i >= r1 + 1 and len(output) < totalItems:
                output.append(matrix[i][c1])
                i -= 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return output
