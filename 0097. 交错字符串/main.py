class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        n1 = len(s1)
        n2 = len(s2)
        if n1+n2 != len(s3):
            return False

        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(1, n1+1):
            if s1[i-1] == s3[i-1] and dp[i-1][0]:
                dp[i][0] = True
        for j in range(1, n2+1):
            if s2[j-1] == s3[j-1] and dp[0][j-1]:
                dp[0][j] = True

        print("dp1")
        print(dp)

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if (dp[i-1][j] and s1[i-1] == s3[j+i-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
        
        print("dp2")
        print(dp)

        return dp[n1][n2]


s = Solution()
print(s.isInterleave("a", "", "a"))
