class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        (x, y), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif board[x][y] == 'E':
                n = sum([board[x + r][y + c] == 'M' for r, c in directions if 0 <= x + r < len(board) and 0 <= y +c < len(board[0])])
                board[x][y] = str(n) if n else 'B'
                for r, c in directions * (not n):
                    self.updateBoard(board, [x + r, y + c])
        return board