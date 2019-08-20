class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = {}
        res, left = 0, 0
        for i in range(len(s)):
            if hashmap.__contains__(s[i]):
                left = hashmap.get(s[i]) if hashmap.get(s[i]) > left else left
            tmp = i - left + 1
            res = tmp if tmp > res else res

            hashmap[s[i]] = i + 1

        return res


s = Solution()
print(s.lengthOfLongestSubstring("fafasd3"))
