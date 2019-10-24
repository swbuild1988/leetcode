class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            res[i][0] = 1
        for j in range(n):
            res[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]

# 还有种解法，排列组合，总共要走m+n-2步，横着走n-1步，插再总共的步数中，C（n-1)(m+n-2),n-1在上面，m+n-2在下面


s = Solution()
print(s.uniquePaths(7, 3))
