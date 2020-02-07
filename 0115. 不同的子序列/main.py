class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        n1 = len(s)
        n2 = len(t)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = 1

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n1][n2]

s = Solution()
print(s.numDistinct("rabbbit", "rabbit"))
