class Solution(object):
    # 暴力法，超时
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.res = 0

        def solve(tmps):
            if len(tmps) == 0:
                self.res += 1
                return

            for i in range(min(len(tmps), 2)):
                if int(tmps[:i+1]) > 0 and int(tmps[:i+1]) <= 26:
                    solve(tmps[i+1:])
                else:
                    return

        solve(s)
        return self.res

    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return 0

        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        if (s[n-1] == '0'):
            dp[n-1] = 0
        else:
            dp[n-1] = 1

        for i in range(n-2, -1, -1):
            if int(s[i]) == 0:
                dp[i] = 0
            else:
                if int(s[i:i+2]) <= 26:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]

        return dp[0]


s = Solution()
print(s.numDecodings2("110"))
