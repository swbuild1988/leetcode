class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0 for i in range(len(s))]
        for i in range(1, len(s), 1):
            if s[i] == ')':
                # 如果前一个为'('，则当前最长的长度为2
                if s[i-1] == '(':
                    dp[i] = 2 + (0 if i-2 < 0 else dp[i-2])
                # 如果前一个为')'，则加上前一个的dp值，再加上
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + (0 if i-dp[i-1] - 2 < 0 else dp[i-dp[i-1]-2])
            else:
                dp[i] = 0
        maxLength = 0
        for i in range(len(dp)):
            maxLength = max(maxLength, dp[i])
        return maxLength


s = Solution()
print(s.longestValidParentheses(")()()))((((()))))"))
