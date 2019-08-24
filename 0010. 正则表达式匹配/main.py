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
        for i in range(2, n+1):
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果是当前值相等或者为'.'，则dp[i][j] = dp[i-1][j-1]
                if (s[i-1] == p[j-1] or p[j-1] == '.'):
                    dp[i][j] = dp[i-1][j-1]
                # 如果为'*'则分两种情况
                # 假设*代表0次，则dp[i][j] = dp[i][j-2],如 ‘ab’和‘abc*’
                # 如果*匹配了至少1次j-1字符，则dp[i][j] = dp[i-1][j]
                # 如'abbb'和'ab*',dp[4][3] = dp[3][3]
                if (p[j-1] == '*'):
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[m][n]


s = Solution()
print(s.isMatch('aab', 'a*'))
