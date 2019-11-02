class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1, n1+1):
            dp[i][0] = i
        for j in range(1, n2+1):
            dp[0][j] = j
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j-1]代表替换字符
                    # dp[i-1][j]代表word1将第i位删除
                    # dp[i][j-1]代表word2增加一个字符
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[n1][n2]

s = Solution()
print(s.minDistance("horse", "ros"))
