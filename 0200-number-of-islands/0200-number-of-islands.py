class Solution:
    def send(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.send(grid, i + 1, j, m, n)
        self.send(grid, i, j + 1, m, n)
        self.send(grid, i - 1, j, m, n)
        self.send(grid, i, j - 1, m, n)

    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.send(grid, i, j, m, n)
                    ans += 1
        return ans
        