class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for j in range(m):
            for i in range(n):
                lives = sum(1 & board[j + dj][i + di]
                            for dj in (-1, 0, 1) for di in (-1, 0, 1)
                            if 0 <= j + dj < m and 0 <= i + di < n
                            ) - board[j][i]
                if board[j][i] and 1 < lives < 4:
                    board[j][i] = 3
                elif not board[j][i] and lives == 3:
                    board[j][i] = 2
        for j in range(m):
            for i in range(n):
                board[j][i] >>= 1