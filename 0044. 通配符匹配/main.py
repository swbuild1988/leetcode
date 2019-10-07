class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1] and p[i-1] == '*'
        print("init")
        print(dp)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果是当前值相等或者为'？'，则dp[i][j] = dp[i-1][j-1]
                if (s[i-1] == p[j-1] or p[j-1] == '?'):
                    dp[i][j] = dp[i-1][j-1]
                # 如果为'*'则分两种情况
                # dp[i][j-1],表示*代表是空字符,例如ab,ab*
                # dp[i-1][j],表示*代表非空任何字符,例如abcd,ab*
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                print("i:", i, "j:", j)
                print(dp)

        return dp[m][n]


s = Solution()
print(s.isMatch("ab", "?*"))
