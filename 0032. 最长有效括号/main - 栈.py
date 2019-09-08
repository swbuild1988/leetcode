class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]
        maxLength = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # 不管如何删掉最后一个，
                # 如果是“（”，则完成一个配对
                # 如果是“）”，说明前面都是没用的了，从当前开始计算有效
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLength = max(maxLength, i-stack[-1])
        return maxLength


s = Solution()
print(s.longestValidParentheses("()()"))
