class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])

        res = [[0 for _ in range(n)] for _ in range(m)]
        f = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                f = 0
            res[i][0] = f
        f = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                f = 0
            res[0][j] = f

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i-1][j] + res[i][j-1]
                else:
                    res[i][j] = 0

        return res[m-1][n-1]

# 还有种解法，排列组合，总共要走m+n-2步，横着走n-1步，插再总共的步数中，C（n-1)(m+n-2),n-1在上面，m+n-2在下面


s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
