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
        if s[0] == 0:
            return 0

        dp = [0 for _ in range(n)]
        dp[0] = 1

        for i in range(1,n):
            if int(s[i]) == 0:
                if int(s[i-1:i+1])> 0 and int(s[i-1:i+1]) < 30:
                    dp[i] = dp[i-1]
                else:
                    return 0
            else:
                dp[i] = dp[i-1]
                if int(s[i-1:i+1])> 10 and int(s[i-1:i+1]) < 30:
                    dp[i] += 1
        
        return dp[n-1]

            

s = Solution()
print(s.numDecodings2("366122"))
