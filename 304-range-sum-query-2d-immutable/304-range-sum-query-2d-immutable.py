class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.newMatrix = []
        if len(matrix) == 0:
            return

        total = [0] * (len(matrix[0]) + 1)
        self.newMatrix.append(total[:])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                total[j+1] += matrix[i][j] + total[j] - self.newMatrix[i][j]
            self.newMatrix.append(total[:])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.newMatrix[row2+1][col2+1] - self.newMatrix[row1][col2+1] - self.newMatrix[row2+1][col1] + self.newMatrix[row1][col1]
    
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)