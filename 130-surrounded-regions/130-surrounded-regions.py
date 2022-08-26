class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        def dfs(i: int, j: int) -> None:
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return
            if board[i][j] != 'O':
                return
            board[i][j] = '*'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i * j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    dfs(i, j)
        for row in board:
            for i, c in enumerate(row):
                if c == '*':
                    row[i] = 'O'
                else:
                    row[i] = 'X'
    