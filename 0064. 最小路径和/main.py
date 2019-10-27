class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            res[i][0] = grid[i][0] + (res[i-1][0] if i > 0 else 0)
        for j in range(n):
            res[0][j] = grid[0][j] + (res[0][j-1] if j > 0 else 0)

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = grid[i][j] + min(res[i-1][j], res[i][j-1])

        return res[m-1][n-1]


s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
