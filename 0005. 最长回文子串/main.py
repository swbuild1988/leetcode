# 中心扩展法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if (length == 0 or length == 1):
            return s

        start, end, maxLen = 0, 0, 0
        for i in range(length):
            len1 = self.findSameLength(s, i, i)
            len2 = self.findSameLength(s, i, i + 1)
            if maxLen < max(len1, len2):
                maxLen = max(len1, len2)
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start: end + 1]

    def findSameLength(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

# 动态规划


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if (length == 0 or length == 1):
            return s
        dp = [[False for i in range(length)] for j in range(length)]
        start, end, maxLen = 0, 0, 0

        for r in range(1, length):
            for l in range(r):
                if (s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1])):
                    dp[l][r] = True
                    if maxLen < r - l + 1:
                        maxLen = r - l + 1
                        start = l
                        end = r
        return s[start: end + 1]


s = Solution2()
print(s.longestPalindrome('aaabaab'))
