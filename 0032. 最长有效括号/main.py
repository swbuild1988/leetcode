class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLength = 0

        # 先从左到右扫描一遍
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, left+right)
            elif right > left:
                right, left = 0, 0

        # 再从右到左扫描一遍
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, left+right)
            elif right < left:
                right, left = 0, 0

        return maxLength


s = Solution()
print(s.longestValidParentheses(")()()))((((()))))"))
